from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any custom fields here
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        db_table = 'auth_user'  # Optional: keeps the same table name
    
    def __str__(self):
        return self.username