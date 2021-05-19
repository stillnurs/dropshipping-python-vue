from utils.permissions.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serialiazers import UserSerializer
from .models import *


class ShoperViewSet(viewsets.ModelViewSet):
    queryset = ShopperProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class VendorViewSet(viewsets.ModelViewSet):
    queryset = VendorProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]





