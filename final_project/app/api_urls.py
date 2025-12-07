from django.urls import path

from .apis import libraries, library, books, book, csrf

"""
URLs for AJAX calls.
Currently not being used.
"""
urlpatterns = [
    path("libraries/", libraries, name="api_libraries"),
    path("libraries/<int:library_id>/", library, name="api_library"),
    path("books/", books, name="api_books"),
    path("books/<int:book_id>/", book, name="api_book"),
    path("csrf/", csrf, name="api_csrf"),
]