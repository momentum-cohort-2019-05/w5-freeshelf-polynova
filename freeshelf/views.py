from django.shortcuts import render

# Create your views here.

from .models import Book, Category
from django.views import generic
from django.http import HttpResponse

# Create your views here.


def index(request):
   """View function for home page of site."""

   list_of_books = Book.objects.all()
   list_of_categories = Category.objects.all()

   context = {
       'list_of_books': list_of_books,
       'list_of_categories': list_of_categories,

   }
   # Render the HTML template index.html with the data in the context variable
   return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
   model = Book


class CategoryDetailView(generic.DetailView):
   model = Category

   