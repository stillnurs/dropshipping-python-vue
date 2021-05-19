from os import name

from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('shoppers', views.ShoperViewSet)
router.register('vendors', views.VendorViewSet)


urlpatterns = [
    path('profile', include(router.urls)),
]