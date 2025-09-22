# library_manager.py

# Import the Book class from the book.py file
from book import Book


def add_book(library):
    """Prompts the user for a book's title, author, and ISBN, creates a new Book object, and adds it to the library list."""
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    isbn = input("Enter the book's ISBN: ")
    new_book = Book(title, author, isbn)
    library.append(new_book)
    print(f"Book '{new_book.title}' added to the library.")


def list_books(library):
    """Iterates through the library list and prints the details of each Book object."""
    if not library:
        print("No books in the library.")
    else:
        print("\n--- Current Library Collection ---")
        for book in library:
            print(book)
        print("----------------------------------\n")


def find_book(library, query):
    """Searches the library list for a book whose title or author matches the provided query."""
    query = query.lower()
    for book in library:
        if query in book.title.lower() or query in book.author.lower():
            return book
    return None


if __name__ == "__main__":
    my_library = [
        Book("The Hobbit", "J.R.R Tolkien", "9780547928227"),
        Book("Pride and Prejudice", "Jane Austen", "9781441341709"),
        Book("Farenheit 451", "Ray Bradburry", "9781451673319"),
        Book("Eragon", "Christopher Paolini", "9780375826696")

    ]

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_book(my_library)
        elif choice == '2':
            list_books(my_library)
        elif choice == '3':
            search_query = input("Enter a title or author to search for: ")
            found_book = find_book(my_library, search_query)
            if found_book:
                print("\nBook found:")
                print(found_book)
            else:
                print("\nBook not found.")
        elif choice == '4':
            print("Exiting the program. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
