Project: Library Management System 
Classes and Objects
Inheritance
Encapsulation
Polymorphism
File Handling (Optional)

Project Description:
This is a simple Library Management System where users can:

Add new books
Issue books to members
Return books
View available books

Implementation Plan:
Step 1: Create a Book class
Attributes: title, author, isbn, available (Boolean)

Methods: display_info(), mark_borrowed(), mark_returned()

Step 2: Create a Library class
Attributes: book_list (A list to store book objects)

Methods:
add_book() – Adds a new book
display_books() – Lists all available books
issue_book() – Marks a book as borrowed
return_book() – Marks a book as returned

Step 3: Create a User class
Attributes: name, user_id, borrowed_books (List of books)
Methods: borrow_book(), return_book(), view_borrowed_books()

Step 4: Create an interactive CLI menu
User can select options to add books, borrow books, return books, and display books.
