from django.db.models import Q
from django.http import Http404
from rest_framework import generics, permissions, renderers
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







class BaseCategoryListView(generics.ListAPIView):
    queryset = BaseCategory.objects.all()
    serializer_class = CategoryPolymorphicSerializer
    permission_classes = [IsOwnerOrReadOnly,]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class BaseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseCategory.objects.all()
    serializer_class = CategoryPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class BaseProductListView(generics.ListAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductPolymorphicSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseProduct.objects.all()
    serializer_class = ProductPolymorphicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    

# Creating an endpoint for the highlighted categories
class BaseCategoryHighlight(generics.GenericAPIView):
    queryset = BaseCategory.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return Response(category.highlighted)



# Creating an endpoint for the highlighted products
class BaseProductHighlight(generics.GenericAPIView):
    queryset = BaseProduct.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(product.highlighted)



# Creating an Endpoint root for API
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'categories': reverse('category-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format)
    })




@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})
