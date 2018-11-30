from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.views import login_required
from books.models import Book, Category
from books.forms import ProposedBookForm
from django.db.models import Count
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.http import JsonResponse


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
    books = books.filter(active=True).select_related('category').annotate(
        num_of_favorites=Count('favorites'))

    favorite_books = []
    if request.user.is_authenticated:
        favorite_books = request.user.favorite_books.all()
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
        body = {"favorite": False}
    else:
        # else create favorite
        book.favorites.create(user=request.user)
        message = f"You have favorited {book}."
        body = {"favorite": True}

    if request.is_ajax():
        return JsonResponse(body)
    else:
        messages.add_message(request, messages.INFO, message)
        return redirect(to='book_list')


def propose_new_book(request):
    if request.method == "POST":
        form = ProposedBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.add_message(
                request, messages.SUCCESS,
                f"Your recommendation of {book} has been noted. Thanks!")
            return redirect(to='book_list')
    else:
        form = ProposedBookForm()

    return render(request, "books/propose_new_book.html", {"form": form})


class AboutView(TemplateView):
    template_name = "about.html"
