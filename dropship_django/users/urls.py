from os import name

from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('^users/list/$', views.UserViewSet, 'user-list')
router.register('^user/{pk}/$', views.UserViewSet, basename='user-detail')


urlpatterns = [
    path('', include(router.urls)),
]
