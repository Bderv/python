class BankAccount:
    def __init__(self, int_rate, balance,):
        self.balance = 0
        self.interest = int_rate
        
        
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    def yield_interest(self):
        if self.balance > 0:
           self.balance = (self.balance * self.interest)+self.balance
        return self
    

class User:
    def __init__(self,name,email):
        self.userID = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    
    def transfer_money(self,userID,amount):
        self.account.balance -= amount
        userID.account.balance += amount
        return self, userID
    
    def display_account_info(self):
        print(f"Hello {self.userID}, your account balance is {self.account.balance}")


user1 = User("Corbin Dallas","5thelement.com")
user2 = User("LeeLu","fromthefuture.com")
user1.account.deposit(500).yield_interest()
user1.display_account_info()
user1.transfer_money(user2, 300)
user1.display_account_info()
user2.display_account_info()



