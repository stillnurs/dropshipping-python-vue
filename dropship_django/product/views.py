from django.db.models import Q
from django.http import Http404
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from management.permissions.permissions import IsOwnerOrReadOnly

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







class CategoryBaseViewSet(viewsets.ModelViewSet):
    queryset = BaseCategory.objects.all()
    serializer_class = CategoryPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    lookup_field = ('slug')

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductBaseViewSet(viewsets.ModelViewSet):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]
    lookup_field = ('slug')
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)







@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = BaseProduct.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = BaseProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
