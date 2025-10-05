# library_management.py

class Book:
    def __init__(self, title: str, author: str):
        # public attributes
        self.title = title
        self.author = author
        # private availability flag
        self._is_checked_out = False

    def check_out(self):
        """
        Mark the book as checked out.
        Returns True if checkout succeeded, False if it was already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Mark the book as returned.
        Returns True if return succeeded, False if it was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        # private list of Book instances
        self._books = []

    def add_book(self, book: Book):
        """Add a Book instance to the library."""
        # avoid duplicates by title-author; still allow different editions if desired
        for b in self._books:
            if b.title == book.title and b.author == book.author:
                return False
        self._books.append(book)
        return True

    def check_out_book(self, title: str):
        """
        Attempt to check out a book by title.
        Returns True if checkout succeeded, False otherwise.
        """
        for b in self._books:
            if b.title == title:
                return b.check_out()
        return False

    def return_book(self, title: str):
        """
        Attempt to return a book by title.
        Returns True if return succeeded, False otherwise.
        """
        for b in self._books:
            if b.title == title:
                return b.return_book()
        return False

    def list_available_books(self):
        """Print available books (title and author) — one per line."""
        for b in self._books:
            if b.is_available():
                print(f"{b.title} by {b.author}")
