from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias
from .forms import Bar_formulario, Restaurante_formulario, Heladeria_formulario, Buscar_formulario

def inicio(request):
    return render(request, 'inicio.html')

def lista_bares(request):
    bares = Bares.objects.all()
    return render(request, 'bares.html', {'listabares': bares})

def lista_restaurantes (request):
    restaurantes = Restaurantes.objects.all()
    return render(request, 'restaurantes.html', {'listarestaurantes': restaurantes})

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

def restaurante_formulario(request):
    if request.method == 'POST':
        mi_formulario = Restaurante_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            restaurante = Restaurantes(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            restaurante.save()
            
            return redirect('Restaurantes')
    else:
        mi_formulario = Restaurante_formulario()

    return render(request, 'restaurante_formulario.html', {'mi_formulario':mi_formulario})

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

def buscar_restaurante (request):
    resto_busqueda= request.GET['restaurante']
    restoran= Restaurantes.objects.filter(nombre=resto_busqueda)
    return render(request, 'resultado_restaurante.html', {'restaurante': restoran, 'query': resto_busqueda})

def buscar_bar (request):
    bar_busqueda= request.GET['bar']
    mi_bar= Bares.objects.filter(nombre=bar_busqueda)
    return render(request, 'resultado_bar.html', {'bar': mi_bar, 'query': bar_busqueda})

def buscar_heladeria (request):
    heladeria_busqueda= request.GET['heladeria']
    mi_heladeria= Heladerias.objects.filter(nombre=heladeria_busqueda)
    return render(request, 'resultado_heladeria.html', {'heladeria': mi_heladeria, 'query': heladeria_busqueda})

