from django.db import models

from factory.models import AbstractDefaultFields, AbstractContacts, AbstractProducts
from retail_network.models import RetailNetwork


class ContactsST(AbstractContacts):
    """Модель контактов ИП"""
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты ИП'

    def __str__(self):
        return f'Контакты {self.city}'


class ProductsST(AbstractProducts):
    """Модель продукции ИП"""
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция ИП'

    def __str__(self):
        return self.title


class SoleTrader(AbstractDefaultFields):
    """Модель индивидуального предпринимателя"""
    supplier = models.ForeignKey(to=RetailNetwork, on_delete=models.CASCADE, verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком', blank=True,
                                           default=0.00)
    contacts = models.ForeignKey(to=ContactsST, on_delete=models.PROTECT, verbose_name='Контакты')
    products = models.ManyToManyField(to=ProductsST, verbose_name='Продукция')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return self.title
