from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Add any custom admin configurations here
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    # Keep the default UserAdmin fieldsets and add custom fields if needed
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone_number', 'date_of_birth')}),
    )