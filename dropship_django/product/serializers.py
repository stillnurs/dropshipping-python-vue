from django.contrib.auth.models import User
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from .models import *


class BaseProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')
    
    class Meta:
        model = BaseProduct
        fields = '__all__'



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'



class MobilePhoneSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MobilePhone
        fields = '__all__'



class BaseCategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='category-highlight', format='html')

    class Meta:
        model = BaseCategory
        fields = '__all__'



class ParentCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ParentCategory
        fields = '__all__'



class ChildCategorySerializer(serializers.HyperlinkedModelSerializer):
    # category = CategorySerializer(many=True)
    
    class Meta:
        model = ChildCategory
        fields = '__all__'




class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # products = BaseProductSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'



class ProductPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseProduct: BaseProductSerializer,
        Product: ProductSerializer,
        MobilePhone: MobilePhoneSerializer
        }



class CategoryPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseCategory: BaseCategorySerializer,
        ParentCategory: ParentCategorySerializer,
        ChildCategory: ChildCategorySerializer,
        Category: CategorySerializer
    }
