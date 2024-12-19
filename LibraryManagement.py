class LibraryManagementSystem:
    def __init__(self):
        # Initialize the list to store book records
        self.books = []  # List to hold all book records
        # Adding 5 books to the library for testing purposes
        self.books.append(
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "isbn": "1234567890", "available": True,
             "reserved": False})
        self.books.append(
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "isbn": "0987654321", "available": True,
             "reserved": False})
        self.books.append(
            {"title": "1984", "author": "George Orwell", "isbn": "1122334455", "available": True, "reserved": False})
        self.books.append(
            {"title": "Pride and Prejudice", "author": "Jane Austen", "isbn": "2233445566", "available": True,
             "reserved": False})
        self.books.append(
            {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "isbn": "3344556677", "available": True,
             "reserved": False})

    def menu(self):
        """Display the main menu and return the user's choice."""
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search for Books")
        print("4. View Available Books")
        print("5. Update Book Information")
        print("6. Exit System")
        choice = input("Enter your choice (1-6): ")  # Get user input for menu choice
        return choice  # Return the user's choice

    def add_book(self):
        """Add a new book to the library."""
        title = input("Enter book title: ")  # Prompt for book title
        author = input("Enter book author: ")  # Prompt for book author
        isbn = input("Enter book ISBN: ")  # Prompt for book ISBN
        # Create a new book record as a dictionary
        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True,  # Initially, the book is available
            "reserved": False  # Initially, the book is not reserved
        }

    def remove_book(self):
        """Remove a book from the library by ISBN."""
        isbn = input("Enter the ISBN of the book to remove: ")  # Prompt for ISBN
        # Iterate through the list of books to find the one to remove
        for book in self.books:
            if book['isbn'] == isbn:  # Check if the ISBN matches
                self.books.remove(book)  # Remove the book from the list
                print(f"Book '{book['title']}' removed successfully.")  # Display success message
                return  # Exit the function after removal
        print("Book not found.")  # Display error if the book is not found

    def search_books(self):
        """Search for books by title or author."""
        search_term = input("Enter title or author to search: ")  # Prompt for search term
        # Search for books that match the search term in title or author
        results = [
            book for book in self.books
            if search_term.lower() in book['title'].lower() or search_term.lower() in book['author'].lower()
        ]
        # Display search results
        if results:
            print("Search Results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            print("No books found.")  # Display message if no books match

    def view_available_books(self):
        """View all available books in the library."""
        # Filter the list of books to find those that are available and not reserved
        available_books = [
            book for book in self.books
            if book['available'] and not book['reserved']
        ]
        # Display available books
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}")
        else:
            print("No available books.")  # Display message if no books are available

    def update_book_information(self):
        """Update the information of a book by ISBN."""
        isbn = input("Enter the ISBN of the book to update: ")  # Prompt for ISBN
        # Iterate through the list of books to find the one to update
        for book in self.books:
            if book['isbn'] == isbn:  # Check if the ISBN matches
                # Prompt for new title and author
                new_title = input("Enter new title (leave blank to keep current): ")
                new_author = input("Enter new author (leave blank to keep current): ")

                # Update title if provided
                if new_title:
                    book['title'] = new_title
                # Update author if provided
                if new_author:
                    book['author'] = new_author

                print(f"Book '{isbn}' updated successfully.")  # Display success message
                return  # Exit the function after updating
        print("Book not found.")  # Display error if the book is not found

    def exit_system(self):
        """Exit the system."""
        print("Exiting the system. Goodbye!")  # Display exit message
        return True  # Indicate that the system is exiting

