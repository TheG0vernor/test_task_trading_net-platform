from rest_framework import viewsets, filters, permissions
from rest_framework.permissions import IsAuthenticated

from sole_trader.models import SoleTrader, ContactsST, ProductsST
from sole_trader.serializers import SoleTraderSerializer, ContactsSTSerializer, ProductsSTSerializer


class SoleTraderViewSet(viewsets.ModelViewSet):
    """Вью индивидуального предпринимателя
    с фильтром по стране и доступом для is_active сотрудников"""
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['contacts__country']
    permission_classes = [IsAuthenticated]


class ContactsSTViewSet(viewsets.ModelViewSet):
    queryset = ContactsST.objects.all()
    serializer_class = ContactsSTSerializer
    permission_classes = [IsAuthenticated]


class ProductsSTViewSet(viewsets.ModelViewSet):
    queryset = ProductsST.objects.all()
    serializer_class = ProductsSTSerializer
    permission_classes = [IsAuthenticated]
