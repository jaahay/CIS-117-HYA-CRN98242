from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, initial_balance=0, fee=10):
        BankAccount.__init__(self, initial_balance)
        self.fee = fee

    def withdraw(self, amt):
        BankAccount.withdraw(self, amt)
        if self.balance < 10000:
            self.balance -= self.fee

    # This method is extending the basic class display
    def display(self):
        print("\n *** Checking Account Statement ***\n")
        BankAccount.display(self)
