"""
shelves  views
"""
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]
    filterset_fields = ('category', 'book_name', 'author', 'publisher',)
    search_fields = ('category', 'book_name', 'author', 'publisher',)
    ordering_fields = '__all__'
    
    def get_queryset(self):
        books = Book.objects.filter(available =True)
        return books
    
class BookDetailView(ListAPIView):
    """
    gets detail of a book
    
    """
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        book = Book.objects.get(id=self.kwargs['book_id'])
        return book
    
    def get(self,request, *args, **kwargs):
        try:
            ser_data = self.serializer_class(instance=self.get_queryset())
            return Response(ser_data.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg':'no such file id'},status=status.HTTP_400_BAD_REQUEST)
    
    
    
    