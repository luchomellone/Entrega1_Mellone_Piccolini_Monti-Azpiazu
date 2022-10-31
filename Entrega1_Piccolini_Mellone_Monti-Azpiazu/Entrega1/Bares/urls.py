from .views import bares, formu, listabares, restaurant, heladeria, bar, inicio, bar_formulario
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bar/<nombre>/<email>/<telefono>', bar),
    path('restaurantes/', restaurant, name="Restaurantes"),
    path('heladerias/', heladeria, name="Heladerias"),
    path('bar-formulario/', bar_formulario, name="bar_formulario"),
    path('buscar/', formu, name ="Formulario_buscar"),
    path('lista-bares/', listabares),
    path('bares', bares, name="Bares"),
]