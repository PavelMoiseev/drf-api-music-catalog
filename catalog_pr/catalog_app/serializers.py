from rest_framework import serializers

from catalog_app.models import Artist, Album, Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all())

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        artist_data = validated_data.pop('artist')
        artist = Artist.objects.get(id=artist_data.id)
        album = Album.objects.create(artist=artist, **validated_data)
        return album


class SongSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        album_data = validated_data.pop('album')
        album = Album.objects.get(id=album_data.id)
        song = Song.objects.create(album=album, **validated_data)
        return song
