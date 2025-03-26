class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_info(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}")

    def mark_borrowed(self):
        if self.available:
            self.available = False
            return True
        return False

    def mark_returned(self):
        self.available = True


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)
        print(f"Book '{book.title}' added successfully!\n")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.book_list:
            book.display_info()

    def issue_book(self, isbn):
        for book in self.book_list:
            if book.isbn == isbn and book.available:
                book.mark_borrowed()
                print(f"Book '{book.title}' issued successfully!\n")
                return book
        print("Book not available or invalid ISBN!\n")
        return None

    def return_book(self, isbn):
        for book in self.book_list:
            if book.isbn == isbn and not book.available:
                book.mark_returned()
                print(f"Book '{book.title}' returned successfully!\n")
                return True
        print("Invalid return request!\n")
        return False


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        book = library.issue_book(isbn)
        if book:
            self.borrowed_books.append(book)

    def return_book(self, library, isbn):
        if any(book.isbn == isbn for book in self.borrowed_books):
            if library.return_book(isbn):
                self.borrowed_books = [book for book in self.borrowed_books if book.isbn != isbn]

    def view_borrowed_books(self):
        print(f"\n{self.name}'s Borrowed Books:")
        for book in self.borrowed_books:
            book.display_info()


def main():
    library = Library()
    user = User("John Doe", 101)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Borrowed Books")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            isbn = input("Enter ISBN to borrow: ")
            user.borrow_book(library, isbn)
        elif choice == "4":
            isbn = input("Enter ISBN to return: ")
            user.return_book(library, isbn)
        elif choice == "5":
            user.view_borrowed_books()
        elif choice == "6":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
