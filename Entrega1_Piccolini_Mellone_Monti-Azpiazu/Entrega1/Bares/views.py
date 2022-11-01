from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias
from .forms import Bar_formulario, Heladeria_formulario, Buscar_formulario

def inicio(request):
    return render(request, 'inicio.html')

def lista_bares(request):
    bares = Bares.objects.all()
    return render(request, 'bares.html', {'listabares': bares})

def lista_restaurantes (request):
    return render(request, 'restaurantes.html')

def lista_heladerias (request):
    heladerias = Heladerias.objects.all()
    return render(request, 'heladerias.html', {'listaheladerias': heladerias})

def bar_formulario(request):
    if request.method == 'POST':
        mi_formulario = Bar_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            bar = Bares(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            bar.save()
            
            return redirect('Bares')
    else:
        mi_formulario = Bar_formulario()

    return render(request, 'bar_formulario.html', {'mi_formulario':mi_formulario})

def heladeria_formulario(request):
    if request.method == 'POST':
        mi_formulario = Heladeria_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            heladeria = Heladerias(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            heladeria.save()
            
            return redirect('Heladerias')
    else:
        mi_formulario = Heladeria_formulario()

    return render(request, 'heladeria_formulario.html', {'mi_formulario':mi_formulario})

def buscar_formulario(request):
    if request.method == 'POST':
        mi_formulario = Buscar_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            bar = Bares(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            bar.save()
            return redirect('Bares')
    else:
        mi_formulario = Buscar_formulario()

    return render(request, 'buscar_formulario.html', {'mi_formulario':mi_formulario})

