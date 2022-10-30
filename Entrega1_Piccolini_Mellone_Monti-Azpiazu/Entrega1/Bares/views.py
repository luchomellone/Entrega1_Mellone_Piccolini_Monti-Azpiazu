from django.shortcuts import render
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias

def inicio(request):
    return render(request, 'inicio.html')

def bar (request, nombre, email, telefono):

    return 

def restaurant (request, nombre, email, telefono):

    return 

def heladeria (request, nombre, email, telefono):

    return 

