from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
books = Book.objects.filter(author__name="Some Author")

# 2. List all books in a library
library_books = Library.objects.get(name="Some Library").books.all()

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=Library.objects.get(name="Some Library"))
