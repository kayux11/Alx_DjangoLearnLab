from django.urls import path
from . import views
from .views import admin_view
from .views import librarian_view
from .views import member_view
from .views import add_book
from .views import edit_book
from .views import delete_book

urlpatterns = [
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based URLs
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Book CRUD URLs (all in same list)
        path('add_book/', add_book, name='add_book'),
        path('edit_book/<int:pk>/', edit_book, name='edit_book'),
        path('delete_book/<int:pk>/', delete_book, name='delete_book'),
    ]
