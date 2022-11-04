from .views import buscar_restaurante, heladeria_formulario, lista_bares, lista_restaurantes, lista_heladerias, inicio, bar_formulario, restaurante_formulario, buscar_bar, buscar_heladeria
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares', lista_bares, name="Bares"),
    path('bar-formulario/', bar_formulario, name="bar_formulario"),
    path('restaurantes/', lista_restaurantes, name="Restaurantes"),
    path('restaurante-formulario/', restaurante_formulario, name="restaurante_formulario"),
    path('heladerias/', lista_heladerias, name="Heladerias"),
    path('heladeria-formulario/', heladeria_formulario, name="heladeria_formulario"),
    path('buscar-restaurante/', buscar_restaurante, name ="buscar_restaurante"),
    path('buscar-bar/', buscar_bar, name ="buscar_bar"),
    path('buscar-heladeria/', buscar_heladeria, name ="buscar_heladeria"),
]