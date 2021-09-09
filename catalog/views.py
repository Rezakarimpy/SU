from django.shortcuts import render
from django.views import generic 

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""



    # Render the HTML template index.html with the data in the context variable
    return render (request, 'index.html')



class BookListView(generic.ListView):
    model = Book