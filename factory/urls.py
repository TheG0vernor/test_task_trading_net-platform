from django.urls import path
from rest_framework import routers

from factory.views import FactoryViewSet, ContactsFactoryViewSet, ProductsFactoryViewSet

router_factory = routers.SimpleRouter()
router_factory.register("", FactoryViewSet, basename='factory')
router_factory.register("contact", ContactsFactoryViewSet, basename='contacts_f')
router_factory.register("product", ProductsFactoryViewSet, basename='products_f')


urlpatterns = [
    path('contact/', ContactsFactoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/', ProductsFactoryViewSet.as_view({'get': 'list', 'post': 'create'})),
]

urlpatterns += router_factory.urls
