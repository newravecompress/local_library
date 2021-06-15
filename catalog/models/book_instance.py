from datetime import date
from django.db import models
from django.contrib.auth import get_user_model
import uuid

from .book import Book

User = get_user_model()


class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True,
                              default='m', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    class Meta:
        ordering = ['due_back']
        permissions = (('can_mark_returned', 'Set book as returned'),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
