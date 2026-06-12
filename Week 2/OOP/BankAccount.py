class BankAccount:
    

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance      

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print(f"[{self.owner}] Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > self.balance:   
            print(f"[{self.owner}] Insufficient funds! "
                  f"Tried ₹{amount}, balance is only ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ₹{amount}. Balance: ₹{self.balance}")

    def display_balance(self):
        print(f"[{self.owner}] Current balance: ₹{self.balance}")



account1 = BankAccount("Ramya", 5000)    
account2 = BankAccount("Priya", 2000)    

print("\n===== BANK ACCOUNT CLASS =====")

account1.display_balance()          
account2.display_balance()          

account1.deposit(1500)              
account1.withdraw(2000)             
account1.withdraw(1000)             

account1.withdraw(9999)             
account2.display_balance()          

account2.deposit(500)               
account2.withdraw(2500)             
account2.withdraw(1)                