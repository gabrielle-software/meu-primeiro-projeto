"""Customer management CLI demo. Do not store real sensitive data."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("customers.json")


def is_valid_customer(customer):
    """Check that a record has a non-empty name and a text contact."""
    return (
        isinstance(customer, dict)
        and isinstance(customer.get("name"), str)
        and bool(customer["name"].strip())
        and isinstance(customer.get("contact", ""), str)
    )


def load_customers():
    """Load valid records, safely handling missing or malformed files."""
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(data, list):
        return []
    return [customer for customer in data if is_valid_customer(customer)]


def save_customers(customers):
    """Persist customer records; return False if writing fails."""
    try:
        DATA_FILE.write_text(
            json.dumps(customers, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except (OSError, TypeError, ValueError):
        print("Error: customers could not be saved.")
        return False
    return True


def add_customer(customers, name, contact=""):
    """Validate and normalize fields before adding a customer."""
    if not isinstance(name, str) or not name.strip():
        return False
    if not isinstance(contact, str):
        return False
    customers.append({"name": name.strip(), "contact": contact.strip()})
    return True


def edit_customer(customers, customer_number, name=None, contact=None):
    """Edit a customer using its 1-based menu number."""
    if not isinstance(customer_number, int) or isinstance(customer_number, bool):
        return False
    index = customer_number - 1
    if index < 0 or index >= len(customers):
        return False
    if name is not None and (not isinstance(name, str) or not name.strip()):
        return False
    if contact is not None and not isinstance(contact, str):
        return False
    if name is not None:
        customers[index]["name"] = name.strip()
    if contact is not None:
        customers[index]["contact"] = contact.strip()
    return True


def delete_customer(customers, customer_number):
    """Delete a customer using its 1-based menu number."""
    if not isinstance(customer_number, int) or isinstance(customer_number, bool):
        return False
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
        contact = customer.get("contact") or "No contact"
        print(f"{number}. {customer['name']} — {contact}")


def read_customer_number(prompt):
    """Read a positive integer selection, or return None if invalid."""
    try:
        number = int(input(prompt).strip())
    except ValueError:
        print("Enter a valid customer number.")
        return None
    if number < 1:
        print("Customer number must be greater than zero.")
        return None
    return number


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
            name = input("Name: ")
            contact = input("Contact (optional): ")
            candidate = [customer.copy() for customer in customers]
            if not add_customer(candidate, name, contact):
                print("Invalid customer data. A name is required.")
                continue
            if save_customers(candidate):
                customers = candidate
                print("Customer saved.")
        elif choice == "2":
            display_customers(customers)
        elif choice == "3":
            display_customers(customers)
            if not customers:
                continue
            number = read_customer_number("Customer number to edit: ")
            if number is None:
                continue
            if number > len(customers):
                print("Customer number is invalid.")
                continue
            name = input("New name (leave blank to keep current): ").strip()
            contact = input("New contact (leave blank to keep current): ").strip()
            candidate = [customer.copy() for customer in customers]
            if not edit_customer(candidate, number, name=name or None, contact=contact or None):
                print("Customer data is invalid.")
                continue
            if save_customers(candidate):
                customers = candidate
                print("Customer updated.")
        elif choice == "4":
            display_customers(customers)
            if not customers:
                continue
            number = read_customer_number("Customer number to delete: ")
            if number is None:
                continue
            if number > len(customers):
                print("Customer number is invalid.")
                continue
            confirmation = input("Confirm deletion? (y/n): ").strip().lower()
            if confirmation == "y":
                candidate = [customer.copy() for customer in customers]
                if delete_customer(candidate, number) and save_customers(candidate):
                    customers = candidate
                    print("Customer deleted.")
            else:
                print("Deletion cancelled.")
        elif choice == "0":
            break
        else:
            print("Choose a listed option.")


if __name__ == "__main__":
    main()
