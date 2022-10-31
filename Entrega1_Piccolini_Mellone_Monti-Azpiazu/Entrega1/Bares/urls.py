from .views import lista_bares, buscar_formulario, lista_restaurantes, lista_heladerias, inicio, bar_formulario
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares', lista_bares, name="Bares"),
    path('restaurantes/', lista_restaurantes, name="Restaurantes"),
    path('heladerias/', lista_heladerias, name="Heladerias"),
    path('bar-formulario/', bar_formulario, name="bar_formulario"),
    path('buscar-formulario/', buscar_formulario, name ="buscar_formulario"),
]