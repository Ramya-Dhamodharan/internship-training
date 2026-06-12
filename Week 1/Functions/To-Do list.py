

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
