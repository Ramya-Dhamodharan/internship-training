class Bank:
    

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance      

    def deposit(self, amount):
        self.balance += amount
        print(f"[{self.owner}] Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:   
            print(f"[{self.owner}] Insufficient funds! ")
        else:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ₹{amount}. Balance: ₹{self.balance}")

    def display_balance(self):
        print(f"[{self.owner}] Current balance: ₹{self.balance}")



                     
             

