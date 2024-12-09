class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        self.available = True
        print(f"'{self.title}' has been returned and is now available.")

    def __str__(self, name):
        return f"'{self.title}' by {self.author} ({self.year}) - {'Available' if self.available else 'Not Available'}"
    
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book titled '{title}' not found in the library.")
        return None

library = Library("City Library")

# Adding books
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Listing books
print("\nBooks in the library:")
library.list_books()

# Borrowing a book
print("\nBorrowing a book:")
book_to_borrow = library.find_book("1984")
if book_to_borrow:
    book_to_borrow.borrow()

# Returning a book
print("\nReturning a book:")
book_to_borrow.return_book()

# Listing books after borrowing and returning
print("\nBooks in the library after updates:")
library.list_books()

