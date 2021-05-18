from os import name

from django.conf.urls import url
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('categories/', views.BaseCategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.BaseCategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/highlight/', views.BaseCategoryHighlight.as_view(), name='category-highlight'),
    path('products/', views.BaseProductListView.as_view(), name='product-list'),
    path('products/<int:category_pk>/<int:pk>', views.BaseProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/highlight/', views.BaseProductHighlight.as_view(), name='product-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
