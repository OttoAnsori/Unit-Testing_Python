from book import Book

class BookManager:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added")
        self._books.append(book)

    def get_all_books(self):
        return self._books[:]

    def remove_book(self, title):
        if not title or not title.strip():
            raise ValueError("Title cannot be null or empty")
        initial_count = len(self._books)
        self._books = [b for b in self._books if b.title.lower() != title.strip().lower()]
        return len(self._books) < initial_count

    def find_books_by_author(self, author):
        if not author or not author.strip():
            raise ValueError("Author cannot be null or empty")
        return [b for b in self._books if b.author.lower() == author.strip().lower()]