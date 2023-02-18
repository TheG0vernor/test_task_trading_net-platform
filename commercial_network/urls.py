from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('factory/', include('factory.urls')),
    path('retail_network/', include('retail_network.urls')),
    path('sole_trader/', include('sole_trader.urls')),
]
