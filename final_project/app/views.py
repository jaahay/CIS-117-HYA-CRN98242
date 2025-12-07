from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LibraryForm, BookForm
from .models import Library, Book, BookUUID, WordSet, Word
from .utils import book_uuid, page_title, calculate_word_frequency, isbn_finder

# Create your views here.

def index(request):
    return render(request, "app/index.html")

def libraries(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid():
            # Process the form data
            library_url = form.cleaned_data['url']
            title = page_title.get_page_title(library_url)
            library, created = Library.objects.get_or_create(page_title=title, url=library_url)
            return HttpResponseRedirect('/app/libraries/')
    return render(request, "app/libraries.html", {"libraries": Library.objects.all()})

def library(request, library_id):
    if request.method == "POST":
        form = BookForm(request.POST)
        # print(form)
        print(form.is_valid())
        if form.is_valid():
            # Process the form data
            url = form.cleaned_data['url']
            text_url = form.cleaned_data['text_url']
            book_uuid_deets = book_uuid.parse_book_for_uuid(url)
            isbn = isbn_finder.find_isbn(book_uuid_deets['title'])
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
                library=Library.objects.get(pk=library_id),
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
            # Additional processing can be done here
            return HttpResponseRedirect('/app/libraries/' + str(library_id) + '/')
    return render(request, "app/library.html", {"library": Library.objects.get(pk=library_id)})

def books(request):
    return render(request, "app/books.html", {"books": Book.objects.all()})

def book(request, book_id):
    return render(request, "app/book.html", {"book": Book.objects.get(pk=book_id)})