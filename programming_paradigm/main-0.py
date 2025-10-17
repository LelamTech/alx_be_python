from bank_account import BankAccount

def main():
    account = BankAccount(1000.0)
    account.deposit(250.0)
    account.withdraw(100.0)
    account.display_balance()

if __name__ == "__main__":
    main()
