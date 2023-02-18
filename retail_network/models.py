from django.db import models


from factory.models import Factory, AbstractProducts, AbstractContacts, AbstractDefaultFields


class ContactsRN(AbstractContacts):
    """Модель контактов розничной сети"""
    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты розничной сети'

    def __str__(self):
        return f'Контакты {self.city}'


class ProductsRN(AbstractProducts):
    """Модель продукции розничной сети"""
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция розничной сети'

    def __str__(self):
        return self.title


class RetailNetwork(AbstractDefaultFields):
    """Модель розничной сети"""
    supplier = models.ForeignKey(to=Factory, on_delete=models.CASCADE, verbose_name='Поставщик')
    debt_to_supplier = models.DecimalField(max_digits=20, decimal_places=2,
                                           verbose_name='Задолженность перед поставщиком', blank=True,
                                           default=0.00)
    contacts = models.ForeignKey(to=ContactsRN, on_delete=models.PROTECT, verbose_name='Контакты')
    products = models.ManyToManyField(to=ProductsRN, verbose_name='Продукция')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return self.title
