from profile.models import User

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['get_image', 'get_thumbnail']      



class BaseProductModelSerializer(serializers.ModelSerializer):
    images = ImageSerializer('images', many=True)
    class Meta:
        model = BaseProductModel
        fields = ['owner', 'url', 'id', 'directory', 'parent_category', 
        'child_category', 'name', 'brand', 'price', 'description',
        'product_type', 'in_stock', 'stock', 'weight', 'images']





class ChildCategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ChildCategory
        fields = ['url', 'id', 'owner', 'parent', 'name', 'description']



class ParentCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentCategory
        fields = ['url', 'id', 'owner', 'directory', 'name', 'description']




class StoreDirectorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StoreDirectory
        fields = ['url', 'id', 'owner', 'store', 'name', 'description']



class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.CharField()

    class Meta:
        model = Store
        fields = ['url', 'id', 'owner', 'name', 'description', 'directories']
