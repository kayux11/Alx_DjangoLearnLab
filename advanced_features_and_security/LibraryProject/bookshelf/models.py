from django.db import models
from django.conf import settings

# -------------------
# Book Model
# -------------------
class Book(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


# -------------------
# Project Model
# -------------------
class Project(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="projects"
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------
# UserProfile Model
# -------------------
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
