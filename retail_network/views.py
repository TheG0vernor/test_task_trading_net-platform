from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from retail_network.models import ContactsRN, ProductsRN, RetailNetwork
from retail_network.serializers import RetailNetworkSerializer, ContactsRNSerializer, ProductsRNSerializer


class RetailNetworkViewSet(viewsets.ModelViewSet):
    """Вью розничной сети с фильтром по стране
    и доступом для is_active сотрудников"""
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [IsAuthenticated]


class ContactsRNViewSet(viewsets.ModelViewSet):
    queryset = ContactsRN.objects.all()
    serializer_class = ContactsRNSerializer
    permission_classes = [IsAuthenticated]


class ProductsRNViewSet(viewsets.ModelViewSet):
    queryset = ProductsRN.objects.all()
    serializer_class = ProductsRNSerializer
    permission_classes = [IsAuthenticated]
