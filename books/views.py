from django.shortcuts import render
from books.models import Book


def book_index(request):
    books = Book.objects.all().order_by('-created_at')
    return render(request, "books/index.html", {"books": books})
