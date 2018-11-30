from django import forms
from books.models import Book


class ProposedBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['category', 'title', 'author', 'url', 'description']

    def save(self, commit=True):
        book = super().save(commit=False)
        book.suggested = True
        book.active = False
        if commit:
            book.save()
        return book
