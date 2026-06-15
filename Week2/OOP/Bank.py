class BankAccount:
    

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



account1 = BankAccount("Ramya", 5000)    
account2 = BankAccount("Priya", 2000)    


account1.display_balance()          
account2.display_balance()          
account1.deposit(1500)              
account1.withdraw(2000)                       
account2.display_balance()                      
             

