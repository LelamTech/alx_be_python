#!/usr/bin/python3
"""
Module for modeling a library system using inheritance and composition.
"""

class Book:
    """Base class representing a book."""

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return string representation of Book."""
        return "Book: {} by {}".format(self.title, self.author)


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return string representation of EBook."""
        return "EBook: {} by {}, File Size: {}KB".format(self.title, self.author, self.file_size)


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return string representation of PrintBook."""
        return "PrintBook: {} by {}, Page Count: {}".format(self.title, self.author, self.page_count)


class Library:
    """Class representing a library using composition."""

    def __init__(self):
        """Initialize Library with an empty book list."""
        self.books = []

    def add_book(self, book):
        """Add a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        """Print all books in the library."""
        for book in self.books:
            print(book)
