from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from .models import Product
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductUserThrottle(UserRateThrottle):
    rate = '20/day'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    throttle_classes = [ProductUserThrottle]
