from django.shortcuts import render
from django.contrib.auth.views import login_required
from books.models import Book
from django.db.models import Count


def book_index(request):
    books = Book.objects.all()
    books = books.annotate(num_of_favorites=Count('favorites'))
    favorite_books = []
    if request.user.is_authenticated:
        favorite_books = request.user.favorite_books.all()
    books = books.order_by('-created_at')
    return render(request, "books/index.html", {
        "books": books,
        "favorite_books": favorite_books
    })


@login_required
def toggle_favorite(request):
    pass
