from django.urls import path

from .views import index, libraries, library, books, book, csrf

urlpatterns = [
    path("", index, name="index"),
    path("libraries/", libraries, name="libraries"),
    path("libraries/<int:library_id>/", library, name="library"),
    path("books/", books, name="books"),
    path("books/<int:book_id>/", book, name="book"),
    path("csrf/", csrf, name="csrf"),
]