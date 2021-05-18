from django.contrib.auth.models import User
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from .models import *


class BaseProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BaseProduct
        fields = '__all__'



class MobilePhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobilePhone
        fields = '__all__'
        



class BaseCategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    # category = serializers.HyperlinkedRelatedField(many=True, view_name='mobilephone-detail', queryset=MobilePhone.objects.all())


    class Meta:
        model = BaseCategory
        fields = '__all__'


class ParentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ParentCategory
        fields = '__all__'


class ChildCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildCategory
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'



class ProductPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseProduct: BaseProductSerializer,
        MobilePhone: MobilePhoneSerializer
        }



class CategoryPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        BaseCategory: BaseCategorySerializer,
        ParentCategory: ParentCategorySerializer,
        ChildCategory: ChildCategorySerializer,
        Category: CategorySerializer
    }
