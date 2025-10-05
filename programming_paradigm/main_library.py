# main_library.py

from library_management import Library

# Create a Library instance
my_library = Library("Community Library")

# Add some books
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
my_library.add_book("1984", "George Orwell")
my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

# Display all books
print("\nAvailable Books:")
my_library.display_books()

# Borrow a book
print("\nBorrowing '1984'...")
my_library.borrow_book("1984")

# Try to borrow the same book again
print("\nAttempting to borrow '1984' again...")
my_library.borrow_book("1984")

# Return a book
print("\nReturning '1984'...")
my_library.return_book("1984")

# Display all books again
print("\nUpdated Book List:")
my_library.display_books()
