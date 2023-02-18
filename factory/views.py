from rest_framework import viewsets

from factory.models import Factory, ContactsFactory, ProductsFactory
from factory.serializers import FactorySerializer, ContactsFactorySerializer, ProductsFactorySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class ContactsFactoryViewSet(viewsets.ModelViewSet):
    queryset = ContactsFactory.objects.all()
    serializer_class = ContactsFactorySerializer


class ProductsFactoryViewSet(viewsets.ModelViewSet):
    queryset = ProductsFactory.objects.all()
    serializer_class = ProductsFactorySerializer
