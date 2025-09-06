from django.urls import path
from .views import list_books, LibraryDetailView
from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    # Function-based view: list all books
    path("books/", list_books, name="list_books"),

    # Class-based view: library detail
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]

urlpatterns = [
    # Existing views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication views
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
]