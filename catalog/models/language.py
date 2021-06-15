from django.db import models


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, unique=True,
                            help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        return self.name
