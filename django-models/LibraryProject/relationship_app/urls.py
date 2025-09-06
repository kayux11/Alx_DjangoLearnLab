from .views import list_books
from .views import LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import list_books
from .views import LibraryDetailView, register
from .views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # Function-based view for listing books
    path('books/', views.list_books, name='list_books'),

    # Class-based view for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Role-based access URLs
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
