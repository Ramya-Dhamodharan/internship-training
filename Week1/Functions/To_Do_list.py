

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




