from Bares.views import restaurant, heladeria, bar, inicio
from django.urls import path


urlpatterns = [
    path('', inicio),
    path('bares/', bar),
    path('restaurantes/', restaurant),
    path('heladerias/', heladeria),
]