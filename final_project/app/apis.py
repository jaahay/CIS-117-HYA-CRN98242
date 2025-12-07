import json

from django.core import serializers
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Library, Book, BookUUID, WordSet, Word

from .utils import book_uuid, page_title, calculate_word_frequency, isbn_finder

"""
AJAX api.
Currently not being used.
"""

def libraries(request):
    """
    Create a new library
    """
    data = json.loads(request.body.decode('utf-8'))
    library_url = data.get("url")
    title = page_title.get_page_title(library_url)
    library, created = Library.objects.get_or_create(page_title=title, url=library_url)
    return JsonResponse(model_to_dict(library))

def library(request, library_id):
    """
    Retrieve a specific library by ID
    """
    return JsonResponse(serializers.serialize("json", Library.objects.get(pk=library_id)))

def books(request):
    """
    Create a new book
    """
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
    res = {}
    res["book_uuid"] = model_to_dict(book_uuid_obj)
    res["book"] = model_to_dict(book_obj)
    res["word_set"] = model_to_dict(word_set)
    return JsonResponse(res)

def book(request, book_id):
    """
    Retrieve a specific book by ID
    """
    book = Book.objects.get(pk=book_id)
    word_set = book.wordset_set.first()
    words = word_set.word_set.all().order_by('-frequency')[:10]
    response_data = {
        'book': {
            'title': book.title,
            'author': book.uuid.author,
            'original_publication': book.uuid.original_publication,
        },
        'words': [
            [
                {'word': word.word, 'frequency': word.frequency} for word in word_set[:10]
            ] for word_set in book.word_set.all()
        ]
    }
    return JsonResponse(response_data)

@ensure_csrf_cookie
def csrf(request):
    """ Provide CSRF token
    """
    csrf_token = get_token(request)
    print(csrf_token)
    return JsonResponse({'csrfToken': csrf_token})