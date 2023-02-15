from django.contrib import admin
from .models import *


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year',)
    list_filter = ('title',)
    search_fields = ('artist', 'title',)


class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'title', 'track_number',)
    list_filter = ('album',)
    search_fields = ('album', 'title',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
