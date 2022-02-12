from django.shortcuts import render
from books.models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer 
    
    
    
#Serileştirici, verileri internet üzerinden tüketilmesi kolay bir biçime dönüştürür,
#tipik olarak JSON'dur ve bir API uç noktasında görüntülenir. 