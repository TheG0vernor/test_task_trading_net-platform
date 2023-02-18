from django.urls import path
from rest_framework import routers

from sole_trader.views import ContactsSTViewSet, ProductsSTViewSet, SoleTraderViewSet

router_sole_trader = routers.SimpleRouter()
router_sole_trader.register("", SoleTraderViewSet, basename='sole_trader')
router_sole_trader.register("contact", ContactsSTViewSet, basename='contacts_st')
router_sole_trader.register("product", ProductsSTViewSet, basename='products_st')


urlpatterns = [
    path('contact/', ContactsSTViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/', ProductsSTViewSet.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router_sole_trader.urls
