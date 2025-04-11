class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def show_info(self):
        return f"[{self.book_id}] {self.title} by {self.author} - {self.copies} copy/copies available"

    def update(self, title=None, author=None, copies=None):
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

    def check_password(self):
        attempt = input(f"Hello {self.name}, please enter your password: ").strip()
        return attempt == self.password

    def show_info(self):
        titles = [book.title for book in self.borrowed_books]
        return f"[{self.member_id}] {self.name} - Borrowed books: {titles}"

    def borrow(self, books):
        borrowed = []
        unavailable = []

        for book in books:
            if book.copies > 0:
                book.copies -= 1
                self.borrowed_books.append(book)
                borrowed.append(book.title)
            else:
                unavailable.append(book.title)

        message = ""
        if borrowed:
            message += f"You borrowed: {', '.join(borrowed)}."
        if unavailable:
            message += f" Sorry, these aren't available: {', '.join(unavailable)}."
        return message

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

        message = ""
        if returned:
            message += f"You returned: {', '.join(returned)}."
        if not_found:
            message += f" These books weren’t in your borrowed list: {', '.join(not_found)}."
        return message


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added!")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return "Book removed!"
        return "Book not found."

    def add_member(self, member):
        self.members.append(member)
        print("Welcome to the library!")

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return "Member removed."
        return "Member not found."

    def member_action(self, member_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if not member:
            return "No such member."

        if not member.check_password():
            return "Wrong password!"

        print(f"\n{member.name}, you currently have {len(member.borrowed_books)} book(s).")

        choice = input("Would you like to borrow or return books? ").strip().lower()
        if choice == "borrow":
            return self.handle_borrow(member)
        elif choice == "return":
            return self.handle_return(member)
        else:
            return "Not a valid option."

    def handle_borrow(self, member):
        print("\nAvailable books:")
        for book in self.books:
            print(book.show_info())

        raw_input = input("Enter the book IDs or titles (comma-separated): ")
        entries = [e.strip() for e in raw_input.split(",")]
        selected = [book for e in entries for book in self.books
                    if str(book.book_id) == e or book.title.lower() == e.lower()]

        if not selected:
            return "No valid books selected."

        print()
        return member.borrow(selected)

    def handle_return(self, member):
        if not member.borrowed_books:
            return "You have no books to return."

        print("\nBooks you've borrowed:")
        for book in member.borrowed_books:
            print(book.show_info())

        raw_input = input("Enter the book IDs or titles to return (comma-separated): ")
        entries = [e.strip() for e in raw_input.split(",")]
        selected = [book for e in entries for book in member.borrowed_books
                    if str(book.book_id) == e or book.title.lower() == e.lower()]

        if not selected:
            return "No valid books selected."

        print()
        return member.return_books(selected)

    def run(self):
        while True:
            print("\n=== Library Menu ===")
            print("1. View books")
            print("2. View members")
            print("3. Add a book")
            print("4. Remove a book")
            print("5. Register a member")
            print("6. Remove a member")
            print("7. Member actions")
            print("8. Exit")

            choice = input("Pick an option (1-8): ").strip()

            if choice == "1":
                for book in self.books:
                    print(book.show_info())
            elif choice == "2":
                for member in self.members:
                    print(member.show_info())
            elif choice == "3":
                try:
                    book_id = int(input("Book ID: "))
                    title = input("Title: ")
                    author = input("Author: ")
                    copies = int(input("Number of copies: "))
                    self.add_book(Book(book_id, title, author, copies))
                except ValueError:
                    print("Invalid input.")
            elif choice == "4":
                try:
                    book_id = int(input("Book ID to remove: "))
                    print(self.remove_book(book_id))
                except ValueError:
                    print("Invalid input.")
            elif choice == "5":
                try:
                    member_id = int(input("Member ID: "))
                    name = input("Name: ")
                    password = input("Password: ")
                    self.add_member(Member(member_id, name, password))
                except ValueError:
                    print("Invalid input.")
            elif choice == "6":
                try:
                    member_id = int(input("Member ID to remove: "))
                    print(self.remove_member(member_id))
                except ValueError:
                    print("Invalid input.")
            elif choice == "7":
                try:
                    member_id = int(input("Enter your member ID: "))
                    print(self.member_action(member_id))
                except ValueError:
                    print("Invalid input.")
            elif choice == "8":
                print("Thanks for using the library system. Goodbye!")
                break
            else:
                print("That's not a valid menu choice.")


# Sample setup and run
if __name__ == "__main__":
    library = Library()
    library.add_book(Book(1, "Python Basics", "John Doe", 5))
    library.add_book(Book(2, "Data Science 101", "Jane Doe", 3))
    library.add_book(Book(3, "Machine Learning", "Alice Smith", 4))
    
    library.add_member(Member(1, "Alice", "1234"))
    
    library.run()
