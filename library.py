from datetime import datetime

# ----------------------------
# 1) Book Categories
# ----------------------------
categories = ["Fiction", "Non-Fiction", "Science", "Biography"]

# ----------------------------
# 2) Books Management
# ----------------------------
books = []

class Book:
    def __init__(self, id, title, author, category):
        self.id = id
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"ID: {self.id} | Title: {self.title} | Author: {self.author} | Category: {self.category}"


def add_book():
    id = int(input("Enter book ID: "))
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")

    book = Book(id, title, author, category)
    books.append(book)
    print("Book added successfully!")


def remove_book():
    id = int(input("Enter book ID to remove: "))
    global books
    books = [b for b in books if b.id != id]
    print("Book removed successfully!")


def show_book():
    id = int(input("Enter book ID: "))
    for book in books:
        if book.id == id:
            print(book)
            return
    print("Book not found!")


def show_all_books():
    if not books:
        print("No books in collection.")
    for book in books:
        print(book)


def search_by_title():
    title = input("Enter title to search: ").lower()
    for book in books:
        if book.title.lower() == title:
            print(book)
            return
    print("Book not found!")


def search_by_author():
    author = input("Enter author name: ").lower()
    found = False
    for book in books:
        if author in book.author.lower():
            print(book)
            found = True
    if not found:
        print("No books found for this author.")


# ----------------------------
# 3) Loans Management
# ----------------------------
loans = []

class Loan:
    def __init__(self, id, borrower):
        self.id = id
        self.borrower = borrower
        self.loan_date = datetime.now()
        self.books = {}  # {book: due_date}
        self.cancelled = False

    def add_book(self, book, due_date):
        self.books[book] = due_date

    def remove_book(self, book):
        if book in self.books:
            del self.books[book]

    def total_books(self):
        return len(self.books)

    def cancel(self):
        self.cancelled = True

    def __str__(self):
        status = "Cancelled" if self.cancelled else "Active"
        result = f"\nLoan ID: {self.id}\nBorrower: {self.borrower}\nDate: {self.loan_date}\nStatus: {status}\nBooks:\n"
        for book, due in self.books.items():
            result += f"  - {book.title} (Due: {due})\n"
        result += f"Total Books: {self.total_books()}\n"
        return result


def add_loan():
    id = int(input("Enter loan ID: "))
    borrower = input("Enter borrower name: ")
    loan = Loan(id, borrower)
    loans.append(loan)
    print("Loan created successfully!")


def remove_loan():
    id = int(input("Enter loan ID to remove: "))
    global loans
    loans = [l for l in loans if l.id != id]
    print("Loan removed successfully!")


def show_loan():
    id = int(input("Enter loan ID: "))
    for loan in loans:
        if loan.id == id:
            print(loan)
            return
    print("Loan not found!")


def add_book_to_loan():
    loan_id = int(input("Enter loan ID: "))
    book_id = int(input("Enter book ID: "))
    due_date = input("Enter due date (YYYY-MM-DD): ")

    loan = next((l for l in loans if l.id == loan_id), None)
    book = next((b for b in books if b.id == book_id), None)

    if loan and book:
        loan.add_book(book, due_date)
        print("Book added to loan!")
    else:
        print("Loan or Book not found!")


def cancel_loan():
    id = int(input("Enter loan ID to cancel: "))
    for loan in loans:
        if loan.id == id:
            loan.cancel()
            print("Loan cancelled!")
            return
    print("Loan not found!")


def show_all_loans():
    if not loans:
        print("No loans available.")
    for loan in loans:
        print(loan)


# ----------------------------
# 4) Menu
# ----------------------------
def menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Show Book")
        print("4. Show All Books")
        print("5. Search by Title")
        print("6. Search by Author")
        print("7. Create Loan")
        print("8. Add Book to Loan")
        print("9. Show Loan")
        print("10. Cancel Loan")
        print("11. Show All Loans")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            show_book()
        elif choice == "4":
            show_all_books()
        elif choice == "5":
            search_by_title()
        elif choice == "6":
            search_by_author()
        elif choice == "7":
            add_loan()
        elif choice == "8":
            add_book_to_loan()
        elif choice == "9":
            show_loan()
        elif choice == "10":
            cancel_loan()
        elif choice == "11":
            show_all_loans()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


menu()
