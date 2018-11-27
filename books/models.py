from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_favorited_by(self, user):
        """Given a user, let us know whether this book is favorited by that user."""
        return self.favorites.filter(user=user).count() > 0

    def __str__(self):
        if self.title and self.author:
            return f"{self.title} by {self.author}"

        return super().__str__()


class Favorite(models.Model):
    book = models.ForeignKey(
        to=Book, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            'book',
            'user',
        )
