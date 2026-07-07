# ==========================================================
#               LIBRARY MANAGEMENT SYSTEM
# ==========================================================


# ==========================================================
# Class 1 : Book
# ==========================================================

# Attributes:
# - book_id (integer)
# - title (string)
# - author (string)
# - available_copies (integer)

# Methods:
# - borrow_book(count)
#     * Borrow requested copies if available.
#     * Reduce available copies.
#     * Return True if successful, else False.
#
# - return_book(count)
#     * Add returned copies back.
#
# - display()
#     * Display all book details.

class Book:

    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow_book(self, count):
        if self.available_copies >= count:
            self.available_copies -= count
            return True
        return False

    def return_book(self, count):
        self.available_copies += count

    def display(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Available Copies : {self.available_copies}")
        print("-" * 40)


# ==========================================================
# Class 2 : BorrowRecord
# ==========================================================

# Attributes:
# - record_id (integer)
# - member_name (string)
# - book (Book object)
# - number_of_books (integer)

# Methods:
# - confirm_borrow()
#     * Attempt to borrow books.
#     * Return True if successful, else False.
#
# - return_borrowed_books()
#     * Return borrowed books.
#
# - display()
#     * Display borrow record details.

class BorrowRecord:

    def __init__(self, record_id, member_name, book, number_of_books):
        self.record_id = record_id
        self.member_name = member_name
        self.book = book
        self.number_of_books = number_of_books
        self.borrowed = False

    def confirm_borrow(self):
        if self.book.borrow_book(self.number_of_books):
            self.borrowed = True
            return True
        return False

    def return_borrowed_books(self):
        if self.borrowed:
            self.book.return_book(self.number_of_books)
            self.borrowed = False

    def display(self):
        print(f"Record ID : {self.record_id}")
        print(f"Member Name : {self.member_name}")
        print(f"Book : {self.book.title}")
        print(f"Books Borrowed : {self.number_of_books}")
        print("-" * 40)


# ==========================================================
# Class 3 : Library
# ==========================================================

# Attributes:
# - name (string)
# - books (list of Book objects)

# Methods:
# - add_book(book)
#     * Add a Book object to the library.
#
# - find_book(book_id)
#     * Search for a book using book_id.
#     * Return Book object if found.
#
# - display_books()
#     * Display all books in the library.
#
# - borrow(record)
#     * Confirm borrowing if copies are available.
#
# - accept_return(record)
#     * Return borrowed books to the library.

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_books(self):
        print(f"\nBooks in {self.name}\n")
        for book in self.books:
            book.display()

    def borrow(self, record):
        if record.confirm_borrow():
            print(f"{record.member_name} borrowed '{record.book.title}' successfully.")
        else:
            print(f"Borrow failed for {record.member_name}. Not enough copies.")

    def accept_return(self, record):
        record.return_borrowed_books()
        print(f"{record.member_name} returned '{record.book.title}'.")


# ==========================================================
# Main Program
# ==========================================================

# Tasks:
# 1. Create a Library object.
# 2. Create at least 3 Book objects.
# 3. Add books to the library.
# 4. Display all books.
# 5. Create at least 2 BorrowRecord objects.
# 6. Borrow books.
# 7. Attempt to borrow more books than available.
# 8. Return one borrowed record.
# 9. Display the final status of all books.


library = Library("City Library")

book1 = Book(101, "Ikigai", "Hector Garcia", 5)
book2 = Book(102, "The Alchemist", "Paulo Coelho", 10)
book3 = Book(103, "Atomic Habits", "James Clear", 3)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

record1 = BorrowRecord(1, "Yuvaraj", book1, 2)
record2 = BorrowRecord(2, "Rahul", book2, 4)
record3 = BorrowRecord(3, "Priya", book3, 10)

library.borrow(record1)
library.borrow(record2)
library.borrow(record3)

record1.display()
record2.display()

library.accept_return(record1)

print("\nFinal Library Status\n")
library.display_books()