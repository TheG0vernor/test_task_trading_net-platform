from rest_framework import serializers

from factory.models import Factory, ContactsFactory, ProductsFactory


# class CreateFactorySerializer(serializers.ModelSerializer):
#     """Сериалайзер создания завода"""
#     class Meta:
#         model = Factory
#         fields = '__all__'
#
#     def create(self, validated_data):
#         retail_network = Factory.objects.create(**validated_data)
#         return retail_network


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
