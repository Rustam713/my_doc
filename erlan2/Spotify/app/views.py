from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import Album, Author, Song

class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()

