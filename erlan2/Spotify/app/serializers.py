from rest_framework import serializers
from .models import Author, Album, Song

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        modul = Album
        fields = ('name', 'id')


class AuthorSerializer(serializers.ModelSerializer):

    albums = AlbumSerializer(many=True)

    class Meta:
        modul = Author
        fields = '__all__'