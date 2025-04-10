class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def display_info(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Copies: {self.copies}"

    def update_book(self, title=None, author=None, copies=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if copies is not None:
            self.copies = copies


class Member:
    def __init__(self, member_id, name, password):
        self.member_id = member_id
        self.name = name
        self.password = password
        self.borrowed_books = []

    def verify_password(self):
        entered_password = input(f"Enter password for {self.name}: ").strip()
        return entered_password == self.password

    def display_info(self):
        return f"ID: {self.member_id}, Name: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"

    def borrow_books(self, books):
        borrowed = []
        not_available = []

        for book in books:
            if book.copies > 0:
                book.copies -= 1
                self.borrowed_books.append(book)
                borrowed.append(book.title)
            else:
                not_available.append(book.title)

        result = f"{self.name} borrowed: {', '.join(borrowed)}." if borrowed else ""
        if not_available:
            result += f" The following books were not available: {', '.join(not_available)}."
        return result

    def return_books(self, books):
        returned = []
        not_found = []

        for book in books:
            if book in self.borrowed_books:
                book.copies += 1
                self.borrowed_books.remove(book)
                returned.append(book.title)
            else:
                not_found.append(book.title)

        result = f"{self.name} returned: {', '.join(returned)}." if returned else ""
        if not_found:
            result += f" The following books were not found in borrowed list: {', '.join(not_found)}."
        return result


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        return "Book added successfully."

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return "Book removed successfully."
        return "Book not found."

    def add_member(self, member):
        self.members.append(member)
        return "Member added successfully."

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return "Member removed successfully."
        return "Member not found."

    def choose_action(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            return "Member not found."

        print(f"\n{member.name}, you currently have {len(member.borrowed_books)} books borrowed.")

        if not member.verify_password():
            return "Incorrect password. Access denied."

        action = input("Would you like to borrow books or return books? (Enter 'borrow' or 'return'): ").strip().lower()

        if action == "borrow":
            return self.issue_books(member)
        elif action == "return":
            return self.return_books(member)
        else:
            return "Invalid action selected."

    def issue_books(self, member):
        print("\nAvailable books:")
        for book in self.books:
            print(book.display_info())

        book_input = input("Enter the book IDs or titles (comma-separated): ").strip().split(",")

        selected_books = []
        for book_entry in book_input:
            book_entry = book_entry.strip()
            book = next((b for b in self.books if str(b.book_id) == book_entry or b.title.lower() == book_entry.lower()), None)
            if book:
                selected_books.append(book)

        if not selected_books:
            return "No valid books selected."

        result = member.borrow_books(selected_books)
        print(f"\n{member.name}, you now have {len(member.borrowed_books)} books borrowed.")
        return result

    def return_books(self, member):
        if not member.borrowed_books:
            return "No books to return."

        print("\nBorrowed books:")
        for book in member.borrowed_books:
            print(book.display_info())

        book_input = input("Enter the book IDs or titles to return (comma-separated): ").strip().split(",")

        selected_books = []
        for book_entry in book_input:
            book_entry = book_entry.strip()
            book = next((b for b in member.borrowed_books if str(b.book_id) == book_entry or b.title.lower() == book_entry.lower()), None)
            if book:
                selected_books.append(book)

        if not selected_books:
            return "No valid books selected."

        result = member.return_books(selected_books)
        print(f"\n{member.name}, you now have {len(member.borrowed_books)} books borrowed.")
        return result

    def display_books(self):
        return [book.display_info() for book in self.books]

    def display_members(self):
        return [member.display_info() for member in self.members]

    def run(self):
        while True:
            print("\n--- Library Menu ---")
            print("1. Display all books")
            print("2. Display all members")
            print("3. Add a book")
            print("4. Remove a book")
            print("5. Add a member")
            print("6. Remove a member")
            print("7. Member actions (borrow/return)")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                for book_info in self.display_books():
                    print(book_info)
            elif choice == "2":
                for member_info in self.display_members():
                    print(member_info)
            elif choice == "3":
                try:
                    book_id = int(input("Enter book ID: "))
                    title = input("Enter title: ").strip()
                    author = input("Enter author: ").strip()
                    copies = int(input("Enter number of copies: "))
                    self.add_book(Book(book_id, title, author, copies))
                    print("Book added.")
                except ValueError:
                    print("Invalid input. Try again.")
            elif choice == "4":
                try:
                    book_id = int(input("Enter book ID to remove: "))
                    print(self.remove_book(book_id))
                except ValueError:
                    print("Invalid input. Try again.")
            elif choice == "5":
                try:
                    member_id = int(input("Enter member ID: "))
                    name = input("Enter member name: ").strip()
                    password = input("Set member password: ").strip()
                    self.add_member(Member(member_id, name, password))
                    print("Member added.")
                except ValueError:
                    print("Invalid input. Try again.")
            elif choice == "6":
                try:
                    member_id = int(input("Enter member ID to remove: "))
                    print(self.remove_member(member_id))
                except ValueError:
                    print("Invalid input. Try again.")
            elif choice == "7":
                try:
                    member_id = int(input("Enter member ID: "))
                    print(self.choose_action(member_id))
                except ValueError:
                    print("Invalid input. Try again.")
            elif choice == "8":
                print("Exiting library system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-8.")


# Run the program
library = Library()
library.add_book(Book(1, "Python Programming", "John Doe", 5))
library.add_book(Book(2, "Data Science", "Jane Doe", 3))
library.add_book(Book(3, "Machine Learning", "Alice Smith", 4))
library.add_member(Member(1, "Alice", "1234"))

# Start menu
library.run()
