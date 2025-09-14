from django.db import models
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="relationship_profile"  # ✅ unique related_name
    )
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
