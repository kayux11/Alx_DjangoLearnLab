from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian




from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
books = Book.objects.filter(author__name="Some Author")

# 2. List all books in a library
library_books = Library.objects.get(name="Some Library").books.all()

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=Library.objects.get(name="Some Library"))
