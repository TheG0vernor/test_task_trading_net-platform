from django.contrib import admin

from retail_network.models import RetailNetwork, ProductsRN, ContactsRN

admin.site.register(ProductsRN)


@admin.action(description='Сбросить задолженность')
def reset_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)


@admin.register(RetailNetwork)
class RetailAdmin(admin.ModelAdmin):
    list_filter = ('contacts__city',)
    list_display = ('title', 'supplier',)
    list_display_links = ('title', 'supplier',)
    actions = [reset_debt]


@admin.register(ContactsRN)
class ContactsAdmin(admin.ModelAdmin):
    list_filter = ('city',)
