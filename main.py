"""Simple customer record demo. Do not store real sensitive data."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("customers.json")


def load_customers():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def save_customers(customers):
    DATA_FILE.write_text(json.dumps(customers, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    customers = load_customers()
    while True:
        print("\n=== Customer Management ===\n1. Add customer\n2. List customers\n0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            contact = input("Contact (optional): ").strip()
            if not name:
                print("Name is required.")
                continue
            customers.append({"name": name, "contact": contact})
            save_customers(customers)
            print("Customer saved.")
        elif choice == "2":
            if not customers:
                print("No customers saved.")
            for number, customer in enumerate(customers, 1):
                print(f"{number}. {customer['name']} — {customer['contact'] or 'No contact'}")
        elif choice == "0":
            break
        else:
            print("Choose a listed option.")


if __name__ == "__main__":
    main()
