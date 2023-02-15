import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Artist, Album, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def artist():
    return Artist.objects.create(name='Test artist')


@pytest.fixture
def album(artist):
    return Album.objects.create(title='Test album', artist=artist, release_year=1969)


@pytest.fixture
def song(album):
    return Song.objects.create(title='Test song', album=album, track_number=1)


# Tests for the model Artist

@pytest.mark.django_db
def test_create_artist(api_client):
    url = reverse('artists-list-create')
    data = {'name': 'New test artist'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Artist.objects.filter(name='New test artist').exists()


@pytest.mark.django_db
def test_retrieve_artist(api_client, artist):
    url = reverse('artist-detail', args=[artist.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    expected_data = ArtistSerializer(artist).data
    assert response.data == expected_data


# Tests for the model Album

@pytest.mark.django_db
def test_create_album(api_client, artist):
    url = reverse('albums-list-create')
    data = {'title': 'New test album',
            'artist': artist.id, 'release_year': 1973}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Album.objects.filter(title='New test album').exists()


@pytest.mark.django_db
def test_retrieve_album(api_client, album):
    url = reverse('album-detail', args=[album.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    expected_data = AlbumSerializer(album).data
    assert response.data == expected_data


# Tests for the model Song

@pytest.mark.django_db
def test_create_song(api_client, album):
    url = reverse('songs-list-create')
    data = {'title': 'New test song', 'album': album.id, 'track_number': 6}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Song.objects.filter(title='New test song').exists()


@pytest.mark.django_db
def test_retrieve_song(api_client, song):
    url = reverse('song-detail', args=[song.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    expected_data = SongSerializer(song).data
    assert response.data == expected_data
