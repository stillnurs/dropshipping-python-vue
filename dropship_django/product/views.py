from django.db.models import Q
from django.http import Http404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *



# class LatestProductsList(APIView):
#     def get(self, request, format=None):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)



# class ProductDetail(APIView):
#     def get_object(self, category_slug, product_slug):
#         try:
#             return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
#         except Product.DoesNotExist:
#             raise Http404
    
#     def get(self, request, category_slug, product_slug, format=None):
#         product = self.get_object(category_slug, product_slug)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)



# class CategoryDetail(APIView):
#     def get_object(self, category_slug):
#         try:
#             return Category.objects.get(slug=category_slug)
#         except Product.DoesNotExist:
#             raise Http404
    
#     def get(self, request, category_slug, format=None):
#         category = self.get_object(category_slug)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)



class BaseCategoryViewSet(ModelViewSet):
    queryset = BaseCategory.objects.all()
    serializer_class = CategoryPolymorphicSerializer



class BaseProductViewSet(ModelViewSet):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductPolymorphicSerializer







@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})