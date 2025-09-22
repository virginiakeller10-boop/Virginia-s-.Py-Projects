class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return (f"Title: {self.title},"
                f" Author: {self.author},"
                f" ISBN: {self.isbn},")

    def get_details(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn}
