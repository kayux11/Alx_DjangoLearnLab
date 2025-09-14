from django.shortcuts import render
from bookshelf.models import Book, Library  # ✅ import from bookshelf
from .models import Author, UserProfile



def book_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/book_list.html", {"books": books})


def library_list(request):
    libraries = Library.objects.all()
    return render(request, "relationship_app/library_list.html", {"libraries": libraries})
