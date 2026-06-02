import json
import os

FILENAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(FILENAME, "w") as f:
        json.dump(contacts, f, indent=4)
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def list_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return
    print("\n--- All Contacts ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print("--------------------")

def search_contact(contacts):
    name = input("Enter name to search: ")
    found = [c for c in contacts if name.lower() in c["name"].lower()]
    if not found:
        print("No contact found!")
        return
    for contact in found:
        print(f"Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    found = [c for c in contacts if name.lower() == c["name"].lower()]
    if not found:
        print("No contact found!")
        return
    contacts.remove(found[0])
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")
def main():
    contacts = load_contacts()
    while True:
        print("\n--- CLI Contact Book ---")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5")

main()