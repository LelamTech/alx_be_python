from book_class import Bank, Book

def main():
    acc = Bank("Ryan", 1000)
    acc.deposit(500)
    acc.withdraw(300)
    print(acc)

    my_book = Book("Python 101", "Guido van Rossum")
    print(my_book)

if __name__ == "__main__":
    main()
