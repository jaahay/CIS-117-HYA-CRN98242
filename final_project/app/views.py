from django.http import HttpResponse
from django.shortcuts import render

from .models import Library, Book

from .utils import page_title

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def libraries(request):
    return HttpResponse(Library.objects)

def library(request, library_id):
    return HttpResponse(Library.objects.get(pk=library_id))

def library_post(request, library_url):
    library = Library.objects.get(url=library_url)
    if(library == None):
        title = page_title.get_page_title(library_url)
        library = Library.objects.create(page_title=title, url=library_url)
    return library

from urllib.request import urlopen

def books(request):
    return HttpResponse(Book.objects)

def book(request, book_id):
    return HttpResponse(Book.objects.get(pk=book_id))