from bank_account import BankAccount

class SavingsAccount(BankAccount):

    def __init__(self, initial_balance=0, rate=0.1):
        BankAccount.__init__(self, initial_balance)
        self.my_rate = rate

    def apply_interest(self):
        self.balance = self.balance + self.balance * self.my_rate

    # This method is extending the basic class display
    def display(self):
        print("\n *** Savings Account Statement ***\n")
        BankAccount.display(self)