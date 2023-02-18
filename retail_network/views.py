from rest_framework import viewsets

from retail_network.models import ContactsRN, ProductsRN, RetailNetwork
from retail_network.serializers import RetailNetworkSerializer, ContactsRNSerializer, ProductsRNSerializer


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class ContactsRNViewSet(viewsets.ModelViewSet):
    queryset = ContactsRN.objects.all()
    serializer_class = ContactsRNSerializer


class ProductsRNViewSet(viewsets.ModelViewSet):
    queryset = ProductsRN.objects.all()
    serializer_class = ProductsRNSerializer
