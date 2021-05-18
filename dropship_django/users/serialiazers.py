from django.contrib.auth.models import User
from product.models import BaseCategory, BaseProduct
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta:
        model = User
        fields = '__all__'
