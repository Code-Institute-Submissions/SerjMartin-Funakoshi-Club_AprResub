from django.shortcuts import render
from .models import Book


def all_books(request):
    """A view to show all books"""

    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'library/library.html', context)

