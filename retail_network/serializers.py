from rest_framework import serializers

from retail_network.models import RetailNetwork, ContactsRN, ProductsRN


class RetailNetworkSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD розничной сети"""
    class Meta:
        model = RetailNetwork
        read_only_fields = ['debt_to_supplier']
        fields = '__all__'


class ContactsRNSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD контактов розничной сети"""
    class Meta:
        model = ContactsRN
        fields = '__all__'


class ProductsRNSerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD продукции розничной сети"""
    class Meta:
        model = ProductsRN
        fields = '__all__'
