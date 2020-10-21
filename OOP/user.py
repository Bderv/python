class User:
    def __init__(self, amount, name):
        self.balance = 0
        self.userID = name
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def transfer_money(self,userID,amount):
        self.balance -= amount
        userID.balance += amount
        return self, userID

user1 = User(2,"Corbin Dallas")
user2 = User(4,"Leelu")
        
user1.deposit(400).withdraw(150).transfer_money(user2,200)

print(user2.balance)