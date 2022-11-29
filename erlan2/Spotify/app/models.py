from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    middle_name = models.CharField(max_length=222)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=222)


class Album(models.Model):
    name = models.CharField(max_length=222)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    date_time = models.DateField()


class Song(models.Model):
    name = models.CharField(max_length=222)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

