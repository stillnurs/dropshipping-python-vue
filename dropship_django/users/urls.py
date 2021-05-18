from os import name

from django.urls import include, path
from django.urls.resolvers import URLPattern
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_root),
    path('list/', views.UserList.as_view(), name='user-list'),
    path('detail/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
