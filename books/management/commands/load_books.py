from django.core.management.base import BaseCommand

initial_books = [
    {
        "title": "A Bite of Python",
        "author": "Swaroop C H",
        "url": "https://python.swaroopch.com/",
        "description": '"A Byte of Python" is a free book on programming using the Python language. '
        "It serves as a tutorial or guide to the Python language for a beginner "
        "audience. If all you know about computers is how to save text files, then "
        "this is the book for you.",
    },
    {
        "title": "CS for All",
        "author": "Christine Alvarado, Zachary Dodds, Geoff Kuenning, Ran Libeskind-Hadas",
        "url": "https://www.cs.hmc.edu/csforall/",
        "description": "This book provides an introduction to computer science as an intellectually "
        "rich and vibrant field rather than focusing exclusively on computer "
        "programming. While programming is certainly an important and pervasive "
        "element of our approach, we emphasize concepts and problem-solving over syntax "
        "and programming language features.",
    },
    {
        "title": "Think Python",
        "author": "Allen B. Downey",
        "url": "http://greenteapress.com/thinkpython2/html/index.html",
        "description": "Think Python is an introduction to Python programming "
        "for beginners. It starts with basic concepts of programming, and is "
        "carefully designed to define all terms when they are first used and to "
        "develop each new concept in a logical progression.",
    },
    {
        "title": "Git From the Bottom Up",
        "author": "John Wiegely",
        "url": "https://jwiegley.github.io/git-from-the-bottom-up/",
        "description": "Learn to understand Git by starting with blobs and working your way up to repositories.",
    },
    {
        "title": "Practical Common Lisp",
        "author": "Peter Siebel",
        "url": "http://www.gigamonkeys.com/book/",
        "description": "If you think the greatest pleasure in programming comes from "
        "getting a lot done with code that simply and clearly expresses your intention, "
        "then programming in Common Lisp is likely to be about the most fun you can have "
        "with a computer. You'll get more done, faster, using it than you would using "
        "pretty much any other language.",
    },
    {
        "title": "Eloquent JavaScript",
        "author": "Marijn Haverbeke",
        "url": "https://eloquentjavascript.net/",
        "description": "This is a book about JavaScript, programming, and the wonders of the digital.",
    },
]


class Command(BaseCommand):
    help = "Load some initial data; clears all existing data."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from books.models import Book, Favorite
        from django.contrib.auth.models import User
        from mimesis import Person

        print("Deleting books...")
        Book.objects.all().delete()

        books = []
        for book_data in initial_books:
            book = Book.objects.create(**book_data)
            books.append(book)
        print("Books loaded.")

        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for _ in range(5):
            user = User.objects.create_user(
                person.username(), person.email(), "password"
            )
            users.append(user)
        print("Users created")

        Favorite.objects.all().delete()
        Favorite.objects.create(book=books[0], user=users[0])
        Favorite.objects.create(book=books[0], user=users[1])
        Favorite.objects.create(book=books[0], user=users[2])
        Favorite.objects.create(book=books[0], user=users[3])
        Favorite.objects.create(book=books[1], user=users[0])
        Favorite.objects.create(book=books[1], user=users[1])
        Favorite.objects.create(book=books[2], user=users[0])
        Favorite.objects.create(book=books[2], user=users[1])
        Favorite.objects.create(book=books[2], user=users[2])
