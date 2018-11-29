from django import forms
from books.models import Book


class ProposedBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'url', 'description']
