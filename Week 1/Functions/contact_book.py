

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




