from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from .models import *



class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'



class MobilePhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = MobilePhone
        fields = '__all__'



class BaseCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BaseCategory
        fields = '__all__'



class ParentCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParentCategory
        fields = '__all__'



class ChildCategorySerializer(serializers.ModelSerializer):
    # category = CategorySerializer(many=True)
    
    class Meta:
        model = ChildCategory
        fields = '__all__'




class CategorySerializer(serializers.ModelSerializer):
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
