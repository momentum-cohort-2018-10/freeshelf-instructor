from django.core.management.base import BaseCommand

initial_categories = [
    {
        "name": "Python",
        "slug": "python"
    },
    {
        "name": "Computer Science",
        "slug": "cs"
    },
    {
        "name": "Git",
        "slug": "git"
    },
    {
        "name": "Lisp",
        "slug": "lisp"
    },
    {
        "name": "JavaScript",
        "slug": "js"
    },
]

initial_books = [
    {
        "title":
        "A Bite of Python",
        "author":
        "Swaroop C H",
        "url":
        "https://python.swaroopch.com/",
        "description":
        '"A Byte of Python" is a free book on programming using the Python language. '
        "It serves as a tutorial or guide to the Python language for a beginner "
        "audience. If all you know about computers is how to save text files, then "
        "this is the book for you.",
        "category":
        "python",
    },
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
        "and programming language features.",
        "category":
        "cs",
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
        "develop each new concept in a logical progression.",
        "category":
        "python",
    },
    {
        "title":
        "Git From the Bottom Up",
        "author":
        "John Wiegely",
        "url":
        "https://jwiegley.github.io/git-from-the-bottom-up/",
        "description":
        "Learn to understand Git by starting with blobs and working your way up to repositories.",
        "category":
        "git",
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
        "pretty much any other language.",
        "category":
        "lisp",
    },
    {
        "title":
        "Eloquent JavaScript",
        "author":
        "Marijn Haverbeke",
        "url":
        "https://eloquentjavascript.net/",
        "description":
        "This is a book about JavaScript, programming, and the wonders of the digital.",
        "category":
        "js",
    },
]


class Command(BaseCommand):
    help = "Load some initial data; clears all existing data."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        from books.models import Book, Favorite, Category
        from django.contrib.auth.models import User
        from mimesis import Person

        print("Deleting categories...")
        Category.objects.all().delete()

        print("Deleting books...")
        Book.objects.all().delete()

        categories = {}
        for cat_data in initial_categories:
            category = Category.objects.create(**cat_data)
            categories[category.slug] = category

        books = []
        for book_data in initial_books:
            cat_slug = book_data.pop('category')
            if cat_slug:
                category = categories[cat_slug]
                book = category.book_set.create(**book_data)
            else:
                book = Book.objects.create(**book_data)

            books.append(book)
        print("Books loaded.")

        print("Deleting users...")
        User.objects.filter(is_superuser=False).delete()

        users = []
        person = Person()
        for _ in range(5):
            user = User.objects.create_user(person.username(), person.email(),
                                            "password")
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
