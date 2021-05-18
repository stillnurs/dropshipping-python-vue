from django.contrib.auth.models import User
from product.models import BaseCategory, BaseProduct
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    categories = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail', read_only=True)
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'categories', 'products']
