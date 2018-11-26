from django.core.management.base import BaseCommand

initial_books = [
    {
        "title":
        "CS for All",
        "author":
        "Christine Alvarado, Zachary Dodds, Geoff Kuenning, Ran Libeskind-Hadas",
        "url":
        "https://www.cs.hmc.edu/csforall/",
        "description":
        "This book provides an introduction to computer science as an intellectually "
        "rich and vibrant field rather than focusing exclusively on computer "
        "programming. While programming is certainly an important and pervasive "
        "element of our approach, we emphasize concepts and problem-solving over syntax "
        "and programming language features."
    },
    {
        "title":
        "Think Python",
        "author":
        "Allen B. Downey",
        "url":
        "http://greenteapress.com/thinkpython2/html/index.html",
        "description":
        "Think Python is an introduction to Python programming "
        "for beginners. It starts with basic concepts of programming, and is "
        "carefully designed to define all terms when they are first used and to "
        "develop each new concept in a logical progression."
    },
    {
        "title":
        "Git From the Bottom Up",
        "author":
        "John Wiegely",
        "url":
        "https://jwiegley.github.io/git-from-the-bottom-up/",
        "description":
        "Learn to understand Git by starting with blobs and working your way up to repositories."
    },
    {
        "title":
        "Practical Common Lisp",
        "author":
        "Peter Siebel",
        "url":
        "http://www.gigamonkeys.com/book/",
        "description":
        "If you think the greatest pleasure in programming comes from "
        "getting a lot done with code that simply and clearly expresses your intention, "
        "then programming in Common Lisp is likely to be about the most fun you can have "
        "with a computer. You'll get more done, faster, using it than you would using "
        "pretty much any other language."
    },
    {
        "title":
        "Two Scoops of Django",
        "author":
        "Audrey Roy and Daniel Greenfeld",
        "url":
        "https://www.twoscoopspress.com/pages/two-scoops-of-django-1-11-faq",
        "description":
        "You like Django? You like ice cream? You like this book."
    }
]


class Command(BaseCommand):
    help = "Load some initial books"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from books.models import Book
        print("Deleting books...")
        Book.objects.all().delete()
        for book_data in initial_books:
            book = Book(**book_data)
            book.save()
        print("Books loaded.")
