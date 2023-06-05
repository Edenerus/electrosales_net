from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from network.models import Product
from network.serializers import ProductSerializer
from network.permissions import IsActiveUser


class ProductListView(ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser, ]


class ProductCreateView(CreateAPIView):
    model = Product
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser, ]
    serializer_class = ProductSerializer


class ProductView(RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser, ]
    serializer_class = ProductSerializer
