from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),
    path("libraries/", views.library_list, name="library_list"),
]
