from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class BaseProductModelSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    images = serializers.HyperlinkedRelatedField(
        view_name='product_image', many=True, read_only=True)

    class Meta:
        model = BaseProductModel
        fields = ('__all__', 'owner', 'images')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'      



class ChildCategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        view_name='child-products', many=True, read_only=True)

    class Meta:
        model = ChildCategory
        fields = ('__all__', 'child-products')



class ParentCategorySerializer(serializers.HyperlinkedModelSerializer):
    child_categories = serializers.HyperlinkedRelatedField(
        view_name='child_categories', many=True, read_only=True)
    class Meta:
        model = ParentCategory
        fields = ('__all__', 'child_categories')



class StoreDirectorySerializer(serializers.HyperlinkedModelSerializer):
    parent_categories = serializers.HyperlinkedRelatedField(
        view_name='parent_categories', many=True, read_only=True)

    class Meta:
        model = ParentCategory
        fields = ('__all__', 'parent_categories')



class StoreSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    directories = serializers.HyperlinkedRelatedField(
        view_name='directories', many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('__all__', 'directories')
