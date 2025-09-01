class Book:
    def __init__(self, title, author, year):
        if not title or not title.strip():
            raise ValueError("Title cannot be null or empty")
        if not author or not author.strip():
            raise ValueError("Author cannot be null or empty")
        if not isinstance(year, int) or not (2000 <= year <= 2100):
            raise ValueError("Year must be an integer between 2000 and 2100")

        self.title = title.strip()
        self.author = author.strip()
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author and self.year == other.year