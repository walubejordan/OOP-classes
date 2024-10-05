class BankAccount:
    # Class variable
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Adds the amount to the balance."""
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        """Subtracts the amount from the balance if there are sufficient funds."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        """Adds interest to the current balance based on the class variable interest_rate."""
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest of {interest}. New balance is {self.balance}.")

    def display_account_info(self):
        """Displays the account holder’s name and the current balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


account = BankAccount("Walube Jordan")
account.deposit(10000)
account.withdraw(2500)
account.apply_interest()
account.display_account_info()

account = BankAccount("Nakya Joan")
account.deposit(15000)
account.withdraw(5000)
account.apply_interest()
account.display_account_info()