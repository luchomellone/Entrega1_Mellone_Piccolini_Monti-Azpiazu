from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bares, Restaurantes, Heladerias
from .forms import Bar_formulario

def inicio(request):
    return render(request, 'inicio.html')

def bar(request, nombre, email, telefono):
    bar = Bares(nombre=nombre, email=email, telefono=telefono)
    bar.save()
    return render(request, "Bares.html")

def listabares(request):
    bares = Bares.objects.all()
    return render(request, 'listabares.html', {"listabares": bares})

def bares(request):
    bares = Bares.objects.all()
    return render(request, 'Bares.html', {'listabares': bares})

def restaurant (request):
    return render(request, 'restaurantes.html')

def heladeria (request):
    return render(request, 'heladerias.html')

def bar_formulario(request):
    if request.method == 'POST':
        mi_formulario = Bar_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            bar = Bares(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            bar.save()
            
            return HttpResponse('/app-bares/')
    else:
        mi_formulario = Bar_formulario()

    return render(request, 'bar_formulario.html', {'mi_formulario':mi_formulario})

def formu(request):
    if request.method == 'POST':
        mi_formulario = Bar_formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            bar = Bares(nombre=data['nombre'], email=data['email'], telefono=data['telefono'])
            bar.save()
            return redirect('Bares')
    else:
        mi_formulario = Bar_formulario()

    return render(request, 'Formulario_buscar.html', {'mi_formulario':mi_formulario})

