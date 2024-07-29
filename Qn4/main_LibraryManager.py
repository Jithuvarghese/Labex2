from LibraryManager import LibraryManager

library = LibraryManager()

# Sample books
books_data = [
    ("1234567890", "Operating Systems: Three Easy Pieces", "Remzi H. Arpaci-Dusseau", "Arpaci-Dusseau Books", 1, 2020),
    ("0987654321", "Data Structures and Algorithms in Python", "Michael T. Goodrich", "Wiley", 2, 2021),
    ("1122334455", "Machine Learning Yearning", "Andrew Ng", "deeplearning.ai", 1, 2023),
    ("2233445566", "Introduction to Algorithms", "Thomas H. Cormen", "MIT Press", 4, 2020),
    ("3344556677", "Python Machine Learning", "Sebastian Raschka", "Packt Publishing", 3, 2022),
]

# Adding books to the library
for isbn, title, author, publisher, volume, year in books_data:
    library.add_book(isbn, title, author, publisher, volume, year)

# Removing a book by ISBN
library.remove_book("1234567890")

# Retrieving book details by ISBN
book_details = library.get_book_details("0987654321")
if book_details:
    print(f"Book Details: {book_details}")

# Searching for books by title
search_results = library.search_books("Data Structures")
print(f"Search Results (by title): {search_results}")

# Listing all books in the library
all_books = library.list_books()
print(f"All Books in the Library: {all_books}")

# Updating book details
library.update_book_details("3344556677", title="Advanced Python Machine Learning", year=2023)

# Checking if a book is available by ISBN
availability = library.check_availability("3344556677")
print(f"Book available: {availability}")
