from django.shortcuts import render
from django.contrib.auth.views import login_required
from books.models import Book
from django.db.models import Count, Q


def book_index(request):
    books = Book.objects.all()
    books = books.annotate(num_of_favorites=Count('favorites'))
    if request.user.is_authenticated:
        books = books.annotate(
            favorite_of_user=Count(
                'favorites', filter=Q(favorites__user=request.user)))
    books = books.order_by('-created_at')
    return render(request, "books/index.html", {"books": books})


@login_required
def toggle_favorite(request):
    pass
