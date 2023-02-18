from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель сотрудника. Наследуется от абстрактного класса"""

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
