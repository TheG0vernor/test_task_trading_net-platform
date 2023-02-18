from django.db import models


class AbstractContacts(models.Model):
    """Абстрактный класс для модели контактов"""
    email = models.EmailField()
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    home_number = models.PositiveSmallIntegerField(verbose_name='номер дома')

    class Meta:
        abstract = True


class ContactsFactory(AbstractContacts):
    """Модель контактов завода"""

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты завода'

    def __str__(self):
        return f'Контакты {self.city}'


class AbstractProducts(models.Model):
    """Абстрактный класс для модели продукции"""
    title = models.CharField(max_length=50, verbose_name='Название')
    product_model = models.CharField(max_length=50, verbose_name='Модель')
    date_released = models.DateField(verbose_name='Дата выхода на рынок')

    class Meta:
        abstract = True


class ProductsFactory(AbstractProducts):
    """Модель продукции завода"""
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция завода'

    def __str__(self):
        return self.title


class AbstractDefaultFields(models.Model):
    """Абстрактный класс,
    используемый в моделях приложений factory, retail_network, sole_trader"""
    class Meta:
        abstract = True
    title = models.CharField(max_length=100, verbose_name='Название')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')


class Factory(AbstractDefaultFields):
    """Модель завода"""
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'
    contacts = models.ForeignKey(to=ContactsFactory, on_delete=models.PROTECT, verbose_name='Контакты')
    products = models.ManyToManyField(to=ProductsFactory, verbose_name='Продукция')

    def __str__(self):
        return self.title
