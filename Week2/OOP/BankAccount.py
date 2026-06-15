class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"{self.owner}'s Balance: ₹{self.balance}")


customers = {
    "ramya": BankAccount("Ramya", 5000),
    "priya": BankAccount("Priya", 3000),
    "anu": BankAccount("Anu", 7000)
}

username = input("Enter username: ").lower()

if username in customers:

    account = customers[username]

    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display_balance()

    else:
        print("Invalid choice")

else:
    print("User not found!")