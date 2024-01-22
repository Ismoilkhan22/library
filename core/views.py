from django.views.generic import ListView

from core.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books.html'
