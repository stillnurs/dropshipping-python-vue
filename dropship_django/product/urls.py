from os import name

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('stores', views.StoreViewSet)
router.register('directories', views.StoreDirectoryViewSet)
router.register('parent-categories', views.ParentCategoryViewSet)
router.register('child-categories', views.ChildCategoryViewSet)
router.register('products', views.BaseProductModelViewSet)


urlpatterns = [
    path('', include(router.urls))
]
