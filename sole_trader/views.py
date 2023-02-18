from rest_framework import viewsets

from sole_trader.models import SoleTrader, ContactsST, ProductsST
from sole_trader.serializers import SoleTraderSerializer, ContactsSTSerializer, ProductsSTSerializer


class SoleTraderViewSet(viewsets.ModelViewSet):
    queryset = SoleTrader.objects.all()
    serializer_class = SoleTraderSerializer


class ContactsSTViewSet(viewsets.ModelViewSet):
    queryset = ContactsST.objects.all()
    serializer_class = ContactsSTSerializer


class ProductsSTViewSet(viewsets.ModelViewSet):
    queryset = ProductsST.objects.all()
    serializer_class = ProductsSTSerializer
