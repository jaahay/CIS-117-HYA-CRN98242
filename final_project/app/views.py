import json

from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Library, Book, BookUUID, WordSet, Word

from .utils import book_uuid, page_title, calculate_word_frequency, isbn_finder

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def libraries(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode('utf-8'))
        library_url = data.get("url")
        title = page_title.get_page_title(library_url)
        library = Library.objects.get_or_create(page_title=title, url=library_url)
        return HttpResponse(f"Library added: {library.page_title} - {library.url}")
    return HttpResponse(Library.objects.all())

def library(request, library_id):
    return HttpResponse(Library.objects.get(pk=library_id))

def books(request):
    if(request.method == "POST"):
        data = json.loads(request.body.decode('utf-8'))
        url = data.get("url")
        text_url = data.get("text_url")
        book_uuid_deets = book_uuid.parse_book_for_uuid(url)
        print(book_uuid_deets)
        isbn = isbn_finder.find_isbn(book_uuid_deets['title'])
        print(isbn)
        book_uuid_obj, created = BookUUID.objects.get_or_create(
            isbn=isbn,
            defaults={
                'url': url,
                'text_url': text_url,
                'title': book_uuid_deets['title'],
                'author': book_uuid_deets['author'],
                'original_publication': book_uuid_deets['original_publication'],
                # 'format': book_uuid_deets['format'],
                # 'edition': book_uuid_deets['edition'],
                # 'pubisher': book_uuid_deets['pubisher'],
                # 'market': book_uuid_deets['market'],
            }
        )
        book_obj, created = Book.objects.get_or_create(
            uuid=book_uuid_obj,
            library=Library.objects.get(pk=data.get("library_id")),
            title=book_uuid_obj.title
        )
        word_set, created = WordSet.objects.get_or_create(book=book_obj)
        words = calculate_word_frequency.calculate_word_frequency(text_url)
        for word, frequency in words.items():
            Word.objects.get_or_create(
                word_set=word_set,
                word=word,
                defaults={'frequency': frequency}
            )
        return HttpResponse(f"Book added: {book_uuid_obj.title} by {book_uuid_obj.author}")
    return HttpResponse(Book.objects.all())

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    word_set = book.wordset_set.first()
    words = word_set.word_set.all().order_by('-frequency')
    response_data = {
        'book': {
            'title': book.title,
            'author': book.uuid.author,
            'original_publication': book.uuid.original_publication,
        },
        'words': [
            {'word': word.word, 'frequency': word.frequency} for word in words
        ]
    }
    return JsonResponse(response_data)

@ensure_csrf_cookie
def csrf(request):
    csrf_token = get_token(request)
    print(csrf_token)
    return JsonResponse({'csrfToken': csrf_token})