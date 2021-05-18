from os import name

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('^categories/list/$', views.CategoryBaseViewSet, 'category-list')
router.register('^categories/{slug:category_slug}/$', views.CategoryBaseViewSet, 'category-detail')
router.register('products/list/$', views.ProductBaseViewSet, 'product-list')
router.register('^products/{slug:category_slug}/{slug:product_slug}/$', views.ProductBaseViewSet, 'product-detail')


urlpatterns = [
    path('', include(router.urls))
]
