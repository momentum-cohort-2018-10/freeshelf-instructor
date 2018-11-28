from django.contrib import admin
from books.models import Book, Category, Favorite


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {'slug': ('name', )}


# Register your models here.
admin.site.register(Book)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Favorite)
