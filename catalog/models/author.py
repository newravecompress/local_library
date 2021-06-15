from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    @property
    def url(self):
        return self.get_absolute_url()

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
