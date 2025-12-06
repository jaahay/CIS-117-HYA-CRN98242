from django.http import HttpResponse

from .models import Library, Book, BookUUID, WordSet, Word

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def libraries(request):
    return HttpResponse(Library.objects.all())

def library(request, library_id):
    return HttpResponse(Library.objects.get(pk=library_id))

def books(request):
    return HttpResponse(Book.objects.all())

def book(request, book_id):
    return HttpResponse(Book.objects.get(pk=book_id))