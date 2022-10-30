from django.shortcuts import render
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias

def inicio(request):
    return render(request, 'inicio.html')

def bar (request):
    return render(request, 'bares.html')

def restaurant (request):
    return render(request, 'restaurantes.html')

def heladeria (request):
    return render(request, 'heladerias.html')

