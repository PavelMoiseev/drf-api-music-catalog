from django.urls import include, path
from rest_framework import routers
from catalog_app import views

app_name = 'catalog_app'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
]