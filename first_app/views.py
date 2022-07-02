from django.shortcuts import render

from first_app.models import Address
from .forms import AddressForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]


# Create your views here.


def inicio(request):
    return render(
        request,
        "index.html",
        {"var": "Mi primera aplicacion de prueba con Django framework"},
    )


def formulario(request):
    forma = AddressForm()
    return render(request, "index.html", {"form": forma.as_p})
