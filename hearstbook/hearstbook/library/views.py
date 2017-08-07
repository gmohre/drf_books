from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Library
from .serializers import BookSerializer, LibrarySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_fields = ('author', 'title', 'price', 'isbn')


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    filter_fields = ('name', 'books')
