from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from network.models import Provider
from network.serializers import ProviderSerializer
from network.permissions import IsActiveUser


class ProviderListView(ListAPIView):
    model = Provider
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated, IsActiveUser, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['country', ]


class ProviderView(RetrieveUpdateDestroyAPIView):
    model = Provider
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser, ]
    serializer_class = ProviderSerializer


class ProviderCreateView(CreateAPIView):
    model = Provider
    queryset = Provider.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser, ]
    serializer_class = ProviderSerializer
