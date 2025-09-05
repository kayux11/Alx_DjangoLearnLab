from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library  # ← Add this import

# Create your views here.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books in this library
        context['books'] = self.object.books.all()
        return context