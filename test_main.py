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

    def test_save_customers_writes_json_file(self):
        customers = [{"name": "João", "contact": "joao@example.com"}]
        main.save_customers(customers)
        saved = json.loads(main.DATA_FILE.read_text(encoding="utf-8"))
        self.assertEqual(saved, customers)

    def test_main_adds_and_saves_customer(self):
        inputs = ["1", "Maria", "maria@example.com", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print"):
            main.main()
        self.assertEqual(
            main.load_customers(),
            [{"name": "Maria", "contact": "maria@example.com"}],
        )

    def test_main_rejects_customer_without_name(self):
        inputs = ["1", "   ", "ignored@example.com", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as output:
            main.main()
        self.assertEqual(main.load_customers(), [])
        output.assert_any_call("Name is required.")

    def test_main_lists_saved_customers(self):
        main.save_customers([{"name": "Carlos", "contact": "carlos@example.com"}])
        inputs = ["2", "0"]
        with patch("builtins.input", side_effect=inputs), patch("builtins.print") as output:
            main.main()
        output.assert_any_call("1. Carlos — carlos@example.com")


if __name__ == "__main__":
    unittest.main()
