import sys
sys.path.append('Week 1/Functions')
sys.path.append('Week2/OOP')
sys.path.append('Week2/OOP_Advanced')

import contact_book
import To_Do_list as todo
from Bank import *
from BankAccount import *
from Student import *
from Animal import *
from Shapes import *


def ContactDemo():
    print("========== CONTACT BOOK ==========")
    print("1. Add contact")
    print("2. Find contact")
    print("3. List all contacts")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        name  = input("Enter name: ")
        phone = input("Enter phone: ")
        contact_book.add_contact(name, phone)
    elif choice == "2":
        name = input("Enter name to search: ")
        contact_book.find_contact(name)
    elif choice == "3":
        contact_book.list_contacts()
    else:
        print("Invalid option.")


def TodoListDemo():
    print("========== TO-DO LIST ==========")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show all tasks")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        description = input("Enter task: ")
        todo.add_task(description)
    elif choice == "2":
        description = input("Enter task to remove: ")
        todo.remove_task(description)
    elif choice == "3":
        todo.show_tasks()
    else:
        print("Invalid option.")


def BankDemo():
    print("========== Bank ==========")

    account1 = Bank("Ramya", 5000)
    account2 = Bank("Priya", 3000)

    account1.display_balance()
    account2.display_balance()
    account1.deposit(1500)
    account1.withdraw(2000)
    account2.display_balance()


def BankAccountDemo():
    print("========== BankAccount ==========")
    customers = {
        "ramya": BankAccount("Ramya", 5000),
        "priya": BankAccount("Priya", 3000),
        "anu":   BankAccount("Anu",   7000),
    }

    username = input("Enter username: ").lower()

    if username in customers:
        account = customers[username]

        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")

        choice = int(input("Enter choice: "))

        if choice == 1:
            try:
                 amount = float(input("Enter amount: "))
            except ValueError:
                print("Please enter a valid amount!")
                return
            account.deposit(amount)
        elif choice == 2:
            try:
                 amount = float(input("Enter amount: "))
            except ValueError:
                print("Please enter a valid amount!")
                return
            account.withdraw(amount)
        elif choice == 3:
            account.display_balance()
        else:
            print("Invalid choice")
    else:
        print("User not found!")


def StudentDemo():
    print("========== Student ==========")

    student1 = Student("Ramya", "A")
    student2 = Student("Priya", "B")

    student1.display_info()
    student2.display_info()

    student1.study()
    student2.study()

    print(f"{student1.name}'s grade: {student1.grade}")

    student2.grade = "A"
    print(f"{student2.name} improved to: {student2.grade}")


def AnimalDemo():
    print("========== Animal ==========")

    dog1 = Dog("Rex",     "Labrador")
    cat1 = Cat("Whiskers","Black")
    dog2 = Dog("Buddy",   "Beagle")

    print(dog1)
    print(cat1)
    dog1.speak()
    cat1.speak()

    animals = [dog1, cat1, dog2]
    for animal in animals:
        animal.speak()


def ShapesDemo():
    print("========== Shapes ==========")

    rect = Rectangle(6, 4)
    circ = Circle(5)

    print(rect)
    print(circ)

    shapes = [rect, circ]
    for shape in shapes:
        print(f"{shape.name} area: {shape.area()}")

while True:
    print("Main Menu")
    print("0. Exit")
    print("1. Contact_Book")
    print("2. To-Do-list")
    print("3. Bank")
    print("4. BankAccount")
    print("5. Student")
    print("6. Animal")
    print("7. Shapes")


    try:
        choice = int(input("Choose an option: "))

        if choice == 0:
            print("Exited")
            break
        elif choice == 1:
            ContactDemo()
        elif choice == 2:
            TodoListDemo()
        elif choice == 3:
            BankDemo()
        elif choice == 4:
            BankAccountDemo()
        elif choice == 5:
            StudentDemo()
        elif choice == 6:
            AnimalDemo()
        elif choice == 7:
            ShapesDemo()
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")
        continue
    finally:
        print("Good Bye!")




