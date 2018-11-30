from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField("URL", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorited_users = models.ManyToManyField(
        to=User, through='Favorite', related_name='favorite_books')
    category = models.ForeignKey(
        to='Category', on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    suggested = models.BooleanField(default=False)

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


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    # pylint:disable=arguments-differ
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
