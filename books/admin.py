from django.contrib import admin
from books.models import Book, Category, Favorite


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name', )}


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'active',
    )


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite)
