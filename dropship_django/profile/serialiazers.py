from django.contrib.auth.models import User
from product.serializers import StoreSerializer
from rest_framework import serializers

from .models import *


class VendorProfileSerializer(serializers.HyperlinkedModelSerializer):
    stores = StoreSerializer()

    class Meta:
        model = VendorProfile
        fields = ('id', 'url', 'profile', 'username', 'email', 'first_name', 'last_name', 'dob', 'phone_number', 'address', 'zipcode', 'created_at', 'stores')




class ShopperProfileSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ShopperProfile
        fields = ('id', 'url', 'profile', 'username', 'email', 'first_name', 'last_name', 'dob', 'phone_number', 'address', 'zipcode', 'created_at')



class UserSerialzer(serializers.HyperlinkedModelSerializer):
    vendor_profile = VendorProfileSerializer()
    shopper_profile = ShopperProfile()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password', 'vendor_profile', 'shopper_profile')
