from .views import buscar, heladeria_formulario, lista_bares, buscar_formulario, lista_restaurantes, lista_heladerias, inicio, bar_formulario, restaurante_formulario
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares', lista_bares, name="Bares"),
    path('bar-formulario/', bar_formulario, name="bar_formulario"),
    path('restaurantes/', lista_restaurantes, name="Restaurantes"),
    path('restaurante-formulario/', restaurante_formulario, name="restaurante_formulario"),
    path('heladerias/', lista_heladerias, name="Heladerias"),
    path('heladeria-formulario/', heladeria_formulario, name="heladeria_formulario"),
    path('buscar-formulario/', buscar_formulario, name ="buscar_formulario"),
    path('buscar/', buscar, name ="buscar"),
]