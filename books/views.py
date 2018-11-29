from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.views import login_required
from books.models import Book, Category
from django.db.models import Count
from django.contrib import messages


def book_index(request):
    books = Book.objects.all()
    return render_book_list(request, "Recently added books", books)


def category_index(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    books = category.book_set.all()
    return render_book_list(request, f'Books in category "{category}"', books,
                            category)


@login_required
def favorites_index(request):
    books = request.user.favorite_books.all()
    return render_book_list(request, 'My favorite books', books)


def render_book_list(request, header, books, category=None):
    books = books.select_related('category')
    books = books.annotate(num_of_favorites=Count('favorites'))
    favorite_books = []
    if request.user.is_authenticated:
        favorite_books = request.user.favorite_books
    books = books.order_by('-created_at')
    return render(
        request, "books/index.html", {
            "category": category,
            "header": header,
            "books": books,
            "categories": Category.objects.all().order_by('name'),
            "favorite_books": favorite_books
        })


@require_POST
@login_required
def toggle_favorite(request, book_id):
    # get the book to toggle favorite on
    book = Book.objects.get(pk=book_id)

    # see if current user has this book as a favorite
    if book in request.user.favorite_books.all():
        # if so, delete favorite
        book.favorites.get(user=request.user).delete()
        message = f"You have unfavorited {book}."
    else:
        # else create favorite
        book.favorites.create(user=request.user)
        message = f"You have favorited {book}."

    messages.add_message(request, messages.INFO, message)
    return redirect(f'/#book-{book.pk}')
