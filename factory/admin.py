from django.contrib import admin

from factory.models import Factory, ContactsFactory, ProductsFactory

admin.site.register(ProductsFactory)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_filter = ('contacts__city',)


@admin.register(ContactsFactory)
class ContactsAdmin(admin.ModelAdmin):
    list_filter = ('city',)
