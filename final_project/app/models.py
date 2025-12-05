from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

"""
Libraries represent different websites
"""
class Library(models.Model):
    page_title = models.CharField(max_length=200)
    url = models.URLField()

"""
The same book may be published across multiple different book formats
"""
class BookFormat(models.TextChoices):
    HARDCOVER = "hardcover", "Hardcover"
    PAPERBACK = "paperback", "Paperback"
    LARGE_PRINT = "large_print", "Large print"
    ePUB = "epub", "Electronic Publication"

"""
What can make two copies of the same book have different ISBNs?
Different formats: A hardcover and a paperback of the same book will have different ISBNs.
Different editions: A new edition (e.g., a revised edition) will have a new ISBN.
Different publishers: If the same title is published by two different companies, each will have a different ISBN.
Different markets: A book sold in one country might have a sticker with a different ISBN for that specific market. 
source - google
"""
class BookUUID(models.Model):
    isbn = models.IntegerField(
        validators=[
            MinLengthValidator(13),
            MaxLengthValidator(13)
        ]
    )
    format = models.CharField(max_length=200, choices=BookFormat)
    edition = models.CharField(max_length=200)
    pubisher = models.CharField(max_length=200)
    market = models.CharField(max_length=200)

"""
Books belong to libraries and have titles
"""
class Book(models.Model):
    uuid = models.ForeignKey(BookUUID, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=200)
    fetched_at = models.DateTimeField()

"""
Books have many words
"""
class WordSet(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

"""
Each word entry can be described ie., by frequency
"""
class Word(models.Model):
    word_set = models.ForeignKey(WordSet, on_delete=models.CASCADE)
    frequency = models.IntegerField()