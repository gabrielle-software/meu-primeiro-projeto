"""Simple customer record demo. Do not store real sensitive data."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("customers.json")


def load_customers():
    if not DATA_FILE.exists():
        return []
    try:
        customers = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return customers if isinstance(customers, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def save_customers(customers):
    DATA_FILE.write_text(
        json.dumps(customers, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def edit_customer(customers, customer_number, name=None, contact=None):
    """Edit a customer using its 1-based menu number."""
    index = customer_number - 1
    if index < 0 or index >= len(customers):
        return False
    if name is not None:
        if not name.strip():
            return False
        customers[index]["name"] = name.strip()
    if contact is not None:
        customers[index]["contact"] = contact.strip()
    return True


def delete_customer(customers, customer_number):
    """Delete a customer using its 1-based menu number."""
    index = customer_number - 1
    if index < 0 or index >= len(customers):
        return False
    del customers[index]
    return True


def display_customers(customers):
    if not customers:
        print("No customers saved.")
        return
    for number, customer in enumerate(customers, 1):
        print(f"{number}. {customer['name']} — {customer.get('contact') or 'No contact'}")


def main():
    customers = load_customers()
    while True:
        print(
            "\n=== Customer Management ==="
            "\n1. Add customer"
            "\n2. List customers"
            "\n3. Edit customer"
            "\n4. Delete customer"
            "\n0. Exit"
        )
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
            display_customers(customers)
        elif choice == "3":
            display_customers(customers)
            if not customers:
                continue
            try:
                number = int(input("Customer number to edit: ").strip())
            except ValueError:
                print("Enter a valid customer number.")
                continue
            name = input("New name (leave blank to keep current): ").strip()
            contact = input("New contact (leave blank to keep current): ").strip()
            if not edit_customer(
                customers,
                number,
                name=name or None,
                contact=contact or None,
            ):
                print("Customer number or name is invalid.")
                continue
            save_customers(customers)
            print("Customer updated.")
        elif choice == "4":
            display_customers(customers)
            if not customers:
                continue
            try:
                number = int(input("Customer number to delete: ").strip())
            except ValueError:
                print("Enter a valid customer number.")
                continue
            if not 1 <= number <= len(customers):
                print("Customer number is invalid.")
                continue
            confirmation = input("Confirm deletion? (y/n): ").strip().lower()
            if confirmation == "y":
                delete_customer(customers, number)
                save_customers(customers)
                print("Customer deleted.")
            else:
                print("Deletion cancelled.")
        elif choice == "0":
            break
        else:
            print("Choose a listed option.")


if __name__ == "__main__":
    main()
