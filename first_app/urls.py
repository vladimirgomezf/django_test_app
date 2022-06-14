from django.urls import path
from .views import formulario

urlpatterns = [
    path('form/', formulario),
    # path('first/add', ),
]
