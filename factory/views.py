from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from factory.models import Factory, ContactsFactory, ProductsFactory
from factory.serializers import FactorySerializer, ContactsFactorySerializer, ProductsFactorySerializer


class FactoryViewSet(viewsets.ModelViewSet):
    """Вью завода с фильтром по стране
    и доступом для is_active сотрудников"""
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [IsAuthenticated]


class ContactsFactoryViewSet(viewsets.ModelViewSet):
    queryset = ContactsFactory.objects.all()
    serializer_class = ContactsFactorySerializer
    permission_classes = [IsAuthenticated]


class ProductsFactoryViewSet(viewsets.ModelViewSet):
    queryset = ProductsFactory.objects.all()
    serializer_class = ProductsFactorySerializer
    permission_classes = [IsAuthenticated]
