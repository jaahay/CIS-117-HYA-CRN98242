from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

"""
Libraries represent different websites
"""
class Library(models.Model):
    page_title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.page_title

class BookFormat(models.TextChoices):
    """
    The same book may be published across multiple different book formats
    """
    HARDCOVER = "hardcover", "Hardcover"
    PAPERBACK = "paperback", "Paperback"
    LARGE_PRINT = "large_print", "Large print"
    ePUB = "epub", "Electronic Publication"

class BookUUID(models.Model):
    """
    What can make two copies of the same book have different ISBNs?
    Different formats: A hardcover and a paperback of the same book will have different ISBNs.
    Different editions: A new edition (e.g., a revised edition) will have a new ISBN.
    Different publishers: If the same title is published by two different companies, each will have a different ISBN.
    Different markets: A book sold in one country might have a sticker with a different ISBN for that specific market. 
    """
    isbn = models.IntegerField(
        validators=[
            MinLengthValidator(13),
            MaxLengthValidator(13)
        ],
        unique=True
    )
    url = models.URLField()
    text_url = models.URLField()
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    original_publication = models.CharField(max_length=200)
    format = models.CharField(max_length=200, choices=BookFormat)
    edition = models.CharField(max_length=200)
    pubisher = models.CharField(max_length=200)
    market = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.isbn)

class Book(models.Model):
    """
    Books belong to libraries and have titles
    """
    uuid = models.ForeignKey(BookUUID, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    fetched_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class WordSet(models.Model):
    """
    Books have many words
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.book.title

class Word(models.Model):
    """
    Each word entry can be described ie., by frequency
    """
    word_set = models.ForeignKey(WordSet, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    frequency = models.IntegerField()
    
    def __str__(self):
        return self.word