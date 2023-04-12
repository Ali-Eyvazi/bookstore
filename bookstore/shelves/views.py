"""
shelves  views
"""

from rest_framework.response import Response
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer


class BooksView(ListAPIView):
    """
    get the books which are in model
    """
    
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ('category', 'book_name', 'author', 'publisher',)
    search_fields = ('category', 'book_name', 'author', 'publisher',)
    ordering_fields = '__all__'
    
    def get_queryset(self):
        books = Book.objects.filter(available =True)
        return books
    
    