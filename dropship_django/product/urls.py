from os import name

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryBaseViewSet)
router.register('products', views.ProductBaseViewSet)


urlpatterns = [
    path('', include(router.urls))
]
