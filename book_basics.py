class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return (f"Title: {self.title},"
                f"Author: {self.author},"
                f"ISBN: {self.isbn}")


my_favorite_book = Book("The Hobbit", "J.R.R Tolkien", "9780547928227")
print(my_favorite_book)
