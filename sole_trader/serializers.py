from rest_framework import serializers

from sole_trader.models import SoleTrader, ProductsST, ContactsST


class SoleTraderSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD ИП"""
    class Meta:
        model = SoleTrader
        read_only_fields = ['debt_to_supplier']
        fields = '__all__'


class ContactsSTSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD контактов ИП"""
    class Meta:
        model = ContactsST
        fields = '__all__'


class ProductsSTSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD продукции ИП"""
    class Meta:
        model = ProductsST
        fields = '__all__'
