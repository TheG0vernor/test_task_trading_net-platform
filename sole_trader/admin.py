from django.contrib import admin

from sole_trader.models import SoleTrader, ProductsST, ContactsST

admin.site.register(ProductsST)


@admin.action(description='Сбросить задолженность')
def reset_debt(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0.00)


@admin.register(SoleTrader)
class SoleTraderAdmin(admin.ModelAdmin):
    list_filter = ('contacts__city',)
    list_display = ('title', 'supplier',)
    list_display_links = ('title', 'supplier',)
    actions = [reset_debt]


@admin.register(ContactsST)
class ContactsAdmin(admin.ModelAdmin):
    list_filter = ('city',)
