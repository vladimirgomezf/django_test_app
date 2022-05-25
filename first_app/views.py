from django.shortcuts import render

# Create your views here.


def inicio(request):
    return render(request, 'index.html', {'var': "Mi primera aplicacion de prueba"})
