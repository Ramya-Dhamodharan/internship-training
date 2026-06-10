# functions.py
# Day 5 exercise: functions, lists, and dictionaries

# ─────────────────────────────────────────
# APP 1: Contact Book (stored in a dictionary)
# ─────────────────────────────────────────

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


# Contact Book menu
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


# ─────────────────────────────────────────
# APP 2: To-Do List (stored in a list)
# ─────────────────────────────────────────

tasks = []


def add_task(description):
    tasks.append(description)
    print(f"Task added: '{description}'")


def remove_task(description):
    if description in tasks:
        tasks.remove(description)
        print(f"Removed: '{description}'")
    else:
        print(f"Task '{description}' not found.")


def show_tasks():
    if not tasks:
        print("No tasks — you're all done!")
        return
    print(f"--- {len(tasks)} task(s) remaining ---")
    for i, task in enumerate(tasks):
        print(f"  {i + 1}. {task}")


# To-Do List menu
print("\n========== TO-DO LIST ==========")
print("1. Add task")
print("2. Remove task")
print("3. Show all tasks")

choice = input("Choose an option (1/2/3): ")

if choice == "1":
    description = input("Enter task: ")
    add_task(description)
elif choice == "2":
    description = input("Enter task to remove: ")
    remove_task(description)
elif choice == "3":
    show_tasks()
else:
    print("Invalid option.")