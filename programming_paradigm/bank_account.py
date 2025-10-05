# bank_account.py

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        # encapsulated balance attribute
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float):
        """Add amount to account_balance."""
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.account_balance += amount

    def withdraw(self, amount: float):
        """Attempt to withdraw amount. Return True if successful, False otherwise."""
        if amount < 0:
            raise ValueError("Withdraw amount must be non-negative.")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance}")
