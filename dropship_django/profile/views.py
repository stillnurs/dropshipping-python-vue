from utils.permissions.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serialiazers import UserSerialzer, VendorProfileSerializer, ShopperProfileSerializer
from .models import *


class ShoperViewSet(viewsets.ModelViewSet):
    queryset = ShopperProfile.objects.all()
    serializer_class = ShopperProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer
