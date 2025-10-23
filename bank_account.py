from savings_account import *
from checking_account import *

class BankAccount:
    'class that implements the functionality of a bank account'
    
    key = 1111 # class variable
    
    def __init__(self, initial_balance):
        self.acc_number = BankAccount.generate_account_number()
        self.balance = initial_balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        self.balance -= amt

    def get_balance(self):
        return self.balance

    def set_balance(self, amt):
        self.balance = amt

    def get_acc_number(self):
        return self.acc_number
    
    def display(self):
        print("\n Net Available Balance=", self.balance)
        
    @classmethod
    def generate_account_number(cls):
        BankAccount.key += 1
        return BankAccount.key
    
if __name__ == "__main__":
    anna_account = SavingsAccount(1000)
    joe_account = SavingsAccount(2000, 0.2)
    anna_account.deposit(500)
    joe_account.deposit(100)
