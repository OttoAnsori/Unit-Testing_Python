import unittest
from book import Book
from bookmanager import BookManager

class TestBookManager(unittest.TestCase):

    def setUp(self):
        """Method ini dijalankan sebelum setiap test."""
        self.book_manager = BookManager()
        self.book1 = Book("Python Crash Course", "Eric Matthes", 2019)
        self.book2 = Book("Automate the Boring Stuff", "Al Sweigart", 2020)
        self.book3 = Book("Fluent Python", "Luciano Ramalho", 2021)
    
    # --- Tes untuk method add_book() ---
    def test_add_book_successfully(self):
        """Test kasus sukses menambahkan buku."""
        self.book_manager.add_book(self.book1)
        self.assertIn(self.book1, self.book_manager.get_all_books())
        self.assertEqual(len(self.book_manager.get_all_books()), 1)

    def test_add_non_book_object_should_raise_error(self):
        """Test kasus gagal: menambahkan objek selain Book harus error."""
        with self.assertRaisesRegex(TypeError, "Only Book objects can be added"):
            self.book_manager.add_book("bukan objek buku")

    # --- Tes untuk method remove_book() ---
    def test_remove_book_successfully(self):
        """Test kasus sukses menghapus buku."""
        self.book_manager.add_book(self.book1)
        self.book_manager.add_book(self.book2)
        
        result = self.book_manager.remove_book("Python Crash Course")
        self.assertTrue(result)
        self.assertNotIn(self.book1, self.book_manager.get_all_books())
        self.assertEqual(len(self.book_manager.get_all_books()), 1)

    def test_remove_book_not_found(self):
        """Test kasus gagal: menghapus buku yang tidak ada."""
        self.book_manager.add_book(self.book1)
        result = self.book_manager.remove_book("Buku Tidak Ada")
        self.assertFalse(result)
        self.assertEqual(len(self.book_manager.get_all_books()), 1)

    def test_remove_book_with_empty_title_should_raise_error(self):
        """Test kasus gagal: menghapus buku dengan judul kosong harus error."""
        with self.assertRaises(ValueError):
            self.book_manager.remove_book("   ")

    # --- Tes untuk method find_books_by_author() ---
    def test_find_books_by_author_successfully(self):
        """Test kasus sukses menemukan buku berdasarkan penulis."""
        self.book_manager.add_book(self.book1)
        self.book_manager.add_book(self.book2)
        
        found_books = self.book_manager.find_books_by_author("Eric Matthes")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0], self.book1)

    def test_find_books_by_author_not_found(self):
        """Test kasus: penulis tidak ditemukan, harus mengembalikan list kosong."""
        found_books = self.book_manager.find_books_by_author("Penulis Fiktif")
        self.assertEqual(len(found_books), 0)

    # --- Tes untuk method get_all_books() ---
    def test_get_all_books(self):
        """Test untuk memastikan get_all_books mengembalikan semua buku."""
        self.book_manager.add_book(self.book1)
        self.book_manager.add_book(self.book2)
        
        all_books = self.book_manager.get_all_books()
        self.assertEqual(len(all_books), 2)
        self.assertIn(self.book1, all_books)
        self.assertIn(self.book2, all_books)

    def test_get_all_books_when_empty(self):
        """Test get_all_books saat tidak ada buku."""
        self.assertEqual(len(self.book_manager.get_all_books()), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)