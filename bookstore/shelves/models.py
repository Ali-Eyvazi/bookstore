"""
shelves model
"""
from django.db import models

# Create your models here.


class Category(models.Model):
    """
    category for books
    """
    name = models.CharField()

    class Meta:
        ordering = ('name')
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    """
    book model
    """
    category = models.ManyToManyField( Category, related_name='books')
    book_name = models.CharField()
    author = models.CharField()
    summary = models.TextField()
    publisher = models.CharField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = 'book_name',

    def __str__(self):
        return str(self.book_name)
