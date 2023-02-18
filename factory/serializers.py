from rest_framework import serializers

from factory.models import Factory, ContactsFactory, ProductsFactory


class FactorySerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD завода"""
    class Meta:
        model = Factory
        fields = '__all__'


class ContactsFactorySerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD контактов завода"""
    class Meta:
        model = ContactsFactory
        fields = '__all__'


class ProductsFactorySerializer(serializers.ModelSerializer):
    """Сериалайзер CRUD продукции завода"""
    class Meta:
        model = ProductsFactory
        fields = '__all__'
