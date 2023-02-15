from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from catalog_app.models import Artist, Album, Song
from catalog_app.serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ApiOverview(GenericAPIView):
    def get(self, arg):
        data = {
            'Music catalog': 'catalog/',
            'Swagger documentation': 'swagger/',
            'Alternative Documentation': 'redoc/',
        }
        return Response(data)


class CatalogApiOverview(GenericAPIView):
    def get(self, arg):
        data = {
            'List of artists': 'artists/',
            'List of albums': 'albums/',
            'List of songs': 'songs/',
            'Select artist': 'artists/<int:id>',
            'Select album': 'albums/<int:id>',
            'Select song': 'songs/<int:id>',
        }
        return Response(data)


class ArtistViewSet(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'id'


class AlbumView(RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field = 'id'


class SongView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'
