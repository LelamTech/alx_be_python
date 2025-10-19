#!/usr/bin/python3
"""
Module for Book class demonstrating Python magic methods
"""

class Book:
    """A class that models a book with title, author, and year"""

    def __init__(self, title, author, year):
        """Constructor that initializes book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation"""
        return "{} by {}, published in {}".format(self.title, self.author, self.year)

    def __repr__(self):
        """Official representation that can recreate the object"""
        return "Book('{}', '{}', {})".format(self.title, self.author, self.year)

    def __del__(self):
        """Destructor that announces when a book object is deleted"""
        print("Deleting {}".format(self.title))
