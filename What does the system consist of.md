What does the system consist of?
Book Class – The books in the library

This class represents a book and keeps track of the following:

book_id: A unique ID for the book.

title: The title of the book.

author: The name of the author.

copies: How many copies are available.

Useful methods:

display_info(): Displays information about the book.

update_book(...): Allows updating the title, author, and number of copies – you decide which fields to change.

Member Class – Library users

This class is used to represent the people who borrow books.

member_id: Unique ID.

name: Name of the member.

password: Used as an access code.

borrowed_books: A list of books borrowed by the member.

Important methods:

verify_password(): Prompts the user for a password.

display_info(): Displays the member and their borrowed books.

borrow_books(...): Attempts to borrow books (shows an error if no copies are available).

return_books(...): Returns books if they are found in the borrowed list.

Library Class – The core of the system

This is where all organization happens – from managing books and members to handling borrowing.

books: List of all books.

members: List of all members.

Key methods:

add_book(...) / remove_book(...): Add or remove books.

add_member(...) / remove_member(...): Add or remove users.

choose_action(...): Start user actions (after password verification).

issue_books(...) / return_books(...): Borrowing and returning.

display_books() / display_members(): Shows an overview.

run(): The main menu – controls the entire experience.

Password Protection

To protect users’ borrowing data, a password is required for borrowing/return actions. If the password is incorrect, the process stops and the user is notified.

How borrowing and returning works

Borrowing books:

The system displays all available books.

The user enters the IDs or titles of the books they want to borrow.

The system updates the inventory and adds the books to the user’s list.

Returning books:

The system only shows the books the user has borrowed.

The user selects which ones to return.

The inventory is updated and the books are removed from the borrowed list.

Menu and User Input

When the program runs, the menu looks like this:

Library Menu

View all books

View all members

Add a book

Remove a book

Add a member

Remove a member

Member functions (borrow/return)

Exit

All selections are made by entering a number from 1 to 8.

Example: Adding a book

Enter book ID: 4  
Enter title: Artificial Intelligence  
Enter author: Alan Turing  
Enter number of copies: 2  

Error Handling

If you type something invalid (e.g., letters instead of numbers), it will be caught using try/except.

The system notifies you if a book or member does not exist.

The user can always try again until valid input is provided.