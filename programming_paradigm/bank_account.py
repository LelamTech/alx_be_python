# bank_account.py

class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        # store balance as a float
        self.account_balance = float(initial_balance)

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount must be non-negative.")
        self.account_balance += amount
        # do not print here — main script handles user messages

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Withdraw amount must be non-negative.")
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        # EXACT expected format: "Current Balance: $<amount with 2 decimals>"
        print(f"Current Balance: ${self.account_balance:.2f}")
