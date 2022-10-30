from .views import restaurant, heladeria, bar, inicio
from django.urls import path


urlpatterns = [
    path('', inicio),
    path('bares/', bar, name="Bares"),
    path('restaurantes/', restaurant, name="Restaurantes"),
    path('heladerias/', heladeria, name="Heladerias"),
]