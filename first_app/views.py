from ast import Add
from django.shortcuts import render
from .forms import AddressForm

# Create your views here.


def inicio(request):
    return render(request, 'index.html', {'var': "Mi primera aplicacion de prueba con Django framework"})


def formulario(request):
    forma = AddressForm()
    return render(request, 'index.html', {'form': forma.as_p})
