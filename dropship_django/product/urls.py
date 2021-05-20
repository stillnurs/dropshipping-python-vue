from os import name

from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'stores', views.StoreViewSet)
router.register(r'directories', views.StoreDirectoryViewSet)
router.register(r'parent-categories', views.ParentCategoryViewSet)
router.register(r'child-categories', views.ChildCategoryViewSet)
router.register(r'products', views.BaseProductModelViewSet)


urlpatterns = [
    path('products/', include(router.urls))
]
