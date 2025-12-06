from django.urls import path

from .views import index, libraries, library, books, book
from .apis import rest_libraries, rest_library, rest_books, rest_book, rest_csrf

urlpatterns = [
    path("", index, name="index"),

    path("libraries/", libraries, name="libraries"),
    path("libraries/<int:library_id>/", library, name="library"),
    path("books/", books, name="books"),
    path("books/<int:book_id>/", book, name="book"),

    path("api/libraries/", rest_libraries, name="libraries"),
    path("api/libraries/<int:library_id>/", rest_library, name="library"),
    path("api/books/", rest_books, name="books"),
    path("api/books/<int:book_id>/", rest_book, name="book"),
    path("api/csrf/", rest_csrf, name="csrf"),
]