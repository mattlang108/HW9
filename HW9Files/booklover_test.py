

import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("The Book of Five Rings", 5)
        self.assertIn("The Book of Five Rings", lover.book_list['book_name'].values)

    def test_2_add_book(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("The Art of War", 4)
        lover.add_book("The Art of War", 4)
        self.assertEqual(len(lover.book_list), 1)

    def test_3_has_read(self): 
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("Dune", 5)
        self.assertTrue(lover.has_read("Dune"))

    def test_4_has_read(self): 
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        self.assertFalse(lover.has_read("The Midnight Library"))

    def test_5_num_books_read(self): 
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("The Science of Spice", 5)
        lover.add_book("Liquid Intelligence", 4)
        self.assertEqual(lover.num_books_read(), 2)

    def test_6_fav_books(self):
        lover = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        lover.add_book("The Alchemist", 5)
        lover.add_book("Brave New World", 3)
        lover.add_book("The Way of the Samurai", 4)

        fav_books = lover.fav_books()
        self.assertTrue(all(rating > 3 for rating in fav_books['book_rating']))

if __name__ == '__main__':
    unittest.main(verbosity=3)
