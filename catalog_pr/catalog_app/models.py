from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_year = models.DateField()


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    track_number = models.IntegerField(unique=True)
