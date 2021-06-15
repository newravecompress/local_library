from django.db import models
from django.urls import reverse

from .genre import Genre
from .author import Author
from .language import Language


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000,
                               help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre,
                                   help_text='Select a genre for this book', blank=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['-title']

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    @property
    def url(self):
        return self.get_absolute_url()

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title
