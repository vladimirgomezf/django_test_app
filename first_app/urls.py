from django.urls import path
from . import  views

urlpatterns = [
    path('form/', views.formulario),

    path('address/', views.address_list),
    path('address/<int:pk>/', views.address_detail),
]
