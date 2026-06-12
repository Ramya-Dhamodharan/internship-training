

contacts = {}


def add_contact(name, phone):
    if name in contacts:
        print(f"Updated {name}'s number to {phone}")
    else:
        print(f"Added contact: {name}")
    contacts[name] = phone


def find_contact(name):
    if name in contacts:
        print(f"Found: {name} → {contacts[name]}")
    else:
        print(f"'{name}' not found in contacts.")


def list_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print(f"--- {len(contacts)} contact(s) ---")
    for name, phone in contacts.items():
        print(f"  {name}: {phone}")



print("========== CONTACT BOOK ==========")
print("1. Add contact")
print("2. Find contact")
print("3. List all contacts")

choice = input("Choose an option (1/2/3): ")

if choice == "1":
    name  = input("Enter name: ")
    phone = input("Enter phone: ")
    add_contact(name, phone)
elif choice == "2":
    name = input("Enter name to search: ")
    find_contact(name)
elif choice == "3":
    list_contacts()
else:
    print("Invalid option.")
