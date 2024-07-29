# LibraryManager.py

class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
        else:
            self.books[isbn] = {
                'title': title,
                'author': author,
                'publisher': publisher,
                'volume': volume,
                'year': year
            }
            print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn in self.books:
            removed_book = self.books.pop(isbn)
            print(f"Book '{removed_book['title']}' removed successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def get_book_details(self, isbn):
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"No book found with ISBN {isbn}.")
            return None

    def search_books(self, search_term, search_by="title"):
        results = []
        for book in self.books.values():
            if search_term.lower() in book[search_by].lower():
                results.append(book)
        return results

    def list_books(self):
        return list(self.books.values())

    def update_book_details(self, isbn, **kwargs):
        book = self.books.get(isbn)
        if book:
            for key, value in kwargs.items():
                if key in book:
                    book[key] = value
            print(f"Book '{book['title']}' updated successfully.")
        else:
            print(f"No book found with ISBN {isbn}.")

    def check_availability(self, isbn):
        return isbn in self.books
