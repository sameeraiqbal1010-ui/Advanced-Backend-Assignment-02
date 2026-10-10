class Library:
    def _init_(self, name):
        self.name = name
        self.books = []  # Stored as a list of strings

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added successfully.")

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"Book '{book_title}' removed successfully.")
        else:
            print(f"Book '{book_title}' not found in the library.")

    def search_book(self, keyword):
        matching_books = [book for book in self.books if keyword.lower() in book.lower()]
        return matching_books

    def display_books(self):
        print(f"\nLibrary Name: {self.name}")
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books collection:")
            for book in self.books:
                print(f"- {book}")

# Testing Question 3 (Sameera's Library)
my_library = "Sameera's Library"
lib = Library(my_library)

# Adding books
lib.add_book("Python Programming")
lib.add_book("Data Structures and Algorithms")
lib.add_book("Advanced Backend Development")

# Displaying all books
lib.display_books()

# Searching for a book
print("\nSearch Results for 'Python':", lib.search_book("Python"))

# Removing a book
lib.remove_book("Python Programming")

# Displaying books after removal
lib.display_books()