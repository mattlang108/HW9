

import pandas as pd

class BookLover:
    def __init__(self, name: str, email: str, fav_genre: str, num_books: int = 0, book_list: pd.DataFrame = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name: str, rating: int):
        if book_name in self.book_list['book_name'].values:
            print(f"You've already added the book: {book_name}")
            return
        
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self, book_name: str) -> bool:
        return book_name in self.book_list['book_name'].values

    def num_books_read(self) -> int:
        return self.num_books

    def fav_books(self) -> pd.DataFrame:
        return self.book_list[self.book_list['book_rating'] > 3]

if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("Percy Jackson", 4)
    test_object.add_book("The Witcher", 3)
    test_object.add_book("The Divine Comedy", 5)
    test_object.add_book("Harry Potter", 5)
    print(test_object.has_read("Percy Jackson"))
    print(test_object.num_books_read())
    print(test_object.fav_books())

