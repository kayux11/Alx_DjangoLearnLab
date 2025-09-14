from django.contrib import admin
from .models import Book, Project, UserProfile

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "published_at"]
    search_fields = ["title", "user__username"]
    list_filter = ["published_at"]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    filter_horizontal = ["members"]
    search_fields = ["name", "members__username"]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "website"]
    search_fields = ["user__username", "website"]
