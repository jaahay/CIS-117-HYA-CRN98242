from django.http import HttpResponse
from django.shortcuts import render

from .models import Library, Book

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def libraries(request):
    return render(request, "app/libraries.html", {"libraries": Library.objects.all()})

def library(request, library_id):
    return render(request, "app/library.html", {"library": Library.objects.get(pk=library_id)})

def books(request):
    return render(request, "app/books.html", {"books": Book.objects.all()})

def book(request, book_id):
    return render(request, "app/book.html", {"book": Book.objects.get(pk=book_id)})