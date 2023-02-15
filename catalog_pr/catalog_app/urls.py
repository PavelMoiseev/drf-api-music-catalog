from django.urls import include, path
from rest_framework import routers
from catalog_app import views

app_name = 'catalog_app'

urlpatterns = [
    path('', views.CatalogApiOverview.as_view()),
    path('artists/', views.ArtistViewSet.as_view(), name='artists-list-create'),
    path('albums/', views.AlbumViewSet.as_view(), name='albums-list-create'),
    path('songs/', views.SongViewSet.as_view(), name='songs-list-create'),
    path('artists/<int:id>', views.ArtistView.as_view(), name='artist-detail'),
    path('albums/<int:id>', views.AlbumView.as_view(), name='album-detail'),
    path('songs/<int:id>', views.SongView.as_view(), name='song-detail'),
]
