from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class BaseProductModelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = serializers.HyperlinkedRelatedField(
        view_name='product_image', many=True, read_only=True)

    class Meta:
        model = BaseProductModel
        fields = ['url', 'id', 'owner', 'parent_category', 
        'child_category', 'name', 'brand', 'price', 'description',
        'product_type', 'in_stock', 'stock', 'weight', 'images']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'      



class ChildCategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='child-products', many=True, read_only=True)

    class Meta:
        model = ChildCategory
        fields = ['url', 'id', 'owner', 'parent', 'name', 'description', 'products']



class ParentCategorySerializer(serializers.HyperlinkedModelSerializer):
    child_categories = serializers.HyperlinkedRelatedField(
        view_name='child_categories', many=True, read_only=True)
    class Meta:
        model = ParentCategory
        fields = ['url', 'id', 'owner', 'directory', 'name', 'description', 'child_categories']




class StoreDirectorySerializer(serializers.HyperlinkedModelSerializer):
    parent_categories = serializers.HyperlinkedRelatedField(
        view_name='parent_categories', many=True, read_only=True)

    class Meta:
        model = StoreDirectory
        fields = ['url', 'id', 'owner', 'store', 'name', 'description', 'parent_categories']



class StoreSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    directories = serializers.HyperlinkedRelatedField(
        view_name='directories', many=True, read_only=True)

    class Meta:
        model = Store
        fields = ['url', 'id', 'owner', 'name', 'description', 'directories']
