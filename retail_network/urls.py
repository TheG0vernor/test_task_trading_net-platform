from django.urls import path
from rest_framework import routers

from retail_network.views import RetailNetworkViewSet, ContactsRNViewSet, ProductsRNViewSet

router_retail_net = routers.SimpleRouter()
router_retail_net.register("", RetailNetworkViewSet, basename='retail_network')
router_retail_net.register("contact", ContactsRNViewSet, basename='contacts_rn')
router_retail_net.register("product", ProductsRNViewSet, basename='products_rn')


urlpatterns = [
    path('contact/', ContactsRNViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/', ProductsRNViewSet.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router_retail_net.urls
