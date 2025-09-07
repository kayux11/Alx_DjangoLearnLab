# Library Project

## Django Admin Setup for Book Model

### Registering the Model

In `bookshelf/admin.py`, the `Book` model is registered with custom configurations:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("publication_year", "author")
    search_fields = ("title", "author")
```

### Superuse Setup

```bash
python manage.py createsuperuser
```

### Accessing Admin

```bash
python manage.py runserver
```
