import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import main


class TestCustomerManagement(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_data_file = main.DATA_FILE
        main.DATA_FILE = Path(self.temp_dir.name) / "customers.json"

    def tearDown(self):
        main.DATA_FILE = self.original_data_file
        self.temp_dir.cleanup()

    def test_load_customers_returns_empty_list_when_file_does_not_exist(self):
        self.assertEqual(main.load_customers(), [])

    def test_load_customers_reads_valid_json(self):
        customers = [{"name": "Ana", "contact": "ana@example.com"}]
        main.DATA_FILE.write_text(json.dumps(customers), encoding="utf-8")
        self.assertEqual(main.load_customers(), customers)

    def test_load_customers_returns_empty_list_for_invalid_json(self):
        main.DATA_FILE.write_text("{invalid json", encoding="utf-8")
        self.assertEqual(main.load_customers(), [])

    def test_load_customers_ignores_invalid_records(self):
        valid = {"name": "Ana", "contact": "ana@example.com"}
        records = [valid, {"name": " ", "contact": ""}, "not a customer",
                   {"name": "Bruno", "contact": 123}]
        main.DATA_FILE.write_text(json.dumps(records), encoding="utf-8")
        self.assertEqual(main.load_customers(), [valid])

    def test_load_customers_rejects_non_list_json(self):
        main.DATA_FILE.write_text(json.dumps({"name": "Ana"}), encoding="utf-8")
        self.assertEqual(main.load_customers(), [])

    def test_save_customers_writes_json_file(self):
        customers = [{"name": "João", "contact": "joao@example.com"}]
        main.save_customers(customers)
        saved = json.loads(main.DATA_FILE.read_text(encoding="utf-8"))
        self.assertEqual(saved, customers)

    def test_add_customer_trims_fields(self):
        customers = []
        self.assertTrue(main.add_customer(customers, " Ana ", " ana@example.com "))
        self.assertEqual(customers, [{"name": "Ana", "contact": "ana@example.com"}])

    def test_add_customer_rejects_blank_name(self):
        self.assertFalse(main.add_customer([], "   ", ""))

    def test_add_customer_rejects_non_text_contact(self):
        self.assertFalse(main.add_customer([], "Ana", 123))

    def test_main_adds_and_saves_customer(self):
        inputs = ["1", "Maria", "maria@example.com", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            main.main()
        self.assertEqual(main.load_customers(), [{"name": "Maria", "contact": "maria@example.com"}])

    def test_main_rejects_customer_without_name(self):
        inputs = ["1", "   ", "ignored@example.com", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as output:
            main.main()
        self.assertEqual(main.load_customers(), [])
        output.assert_any_call("Invalid customer data. A name is required.")

    def test_main_lists_saved_customers(self):
        main.save_customers([{"name": "Carlos", "contact": "carlos@example.com"}])
        inputs = ["2", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as output:
            main.main()
        output.assert_any_call("1. Carlos — carlos@example.com")

    def test_edit_customer_updates_name_and_contact(self):
        customers = [{"name": "Ana", "contact": "ana@example.com"}]
        self.assertTrue(main.edit_customer(customers, 1, "Beatriz", "bia@example.com"))
        self.assertEqual(customers, [{"name": "Beatriz", "contact": "bia@example.com"}])

    def test_edit_customer_rejects_invalid_number(self):
        customers = [{"name": "Ana", "contact": ""}]
        self.assertFalse(main.edit_customer(customers, 2, "Beatriz", ""))
        self.assertEqual(customers[0]["name"], "Ana")

    def test_edit_customer_rejects_blank_name(self):
        customers = [{"name": "Ana", "contact": ""}]
        self.assertFalse(main.edit_customer(customers, 1, "   ", None))
        self.assertEqual(customers[0]["name"], "Ana")

    def test_edit_customer_rejects_non_text_contact(self):
        self.assertFalse(main.edit_customer([{"name": "Ana", "contact": ""}], 1, None, 123))

    def test_delete_customer_removes_selected_record(self):
        customers = [{"name": "Ana", "contact": ""}, {"name": "Bruno", "contact": "bruno@example.com"}]
        self.assertTrue(main.delete_customer(customers, 1))
        self.assertEqual(customers, [{"name": "Bruno", "contact": "bruno@example.com"}])

    def test_delete_customer_rejects_invalid_number(self):
        customers = [{"name": "Ana", "contact": ""}]
        self.assertFalse(main.delete_customer(customers, 0))
        self.assertEqual(len(customers), 1)

    def test_delete_customer_rejects_non_integer_number(self):
        self.assertFalse(main.delete_customer([{"name": "Ana", "contact": ""}], "1"))

    def test_main_edits_and_saves_customer(self):
        main.save_customers([{"name": "Ana", "contact": "ana@example.com"}])
        inputs = ["3", "1", "Beatriz", "bia@example.com", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            main.main()
        self.assertEqual(main.load_customers(), [{"name": "Beatriz", "contact": "bia@example.com"}])

    def test_main_confirms_and_saves_customer_deletion(self):
        main.save_customers([{"name": "Ana", "contact": "ana@example.com"}])
        inputs = ["4", "1", "y", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            main.main()
        self.assertEqual(main.load_customers(), [])


if __name__ == "__main__":
    unittest.main()
