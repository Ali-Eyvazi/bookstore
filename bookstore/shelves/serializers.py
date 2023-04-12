"""
shelves serializer
"""
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """
    serializer for book model
    """
    class Meta:
        model = Book
        fields = '__all__'
