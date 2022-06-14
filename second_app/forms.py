from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from django import forms

from second_app.models import Persona


class PersonaForm(Forms.form):
    nombre = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'})),
    # 'apellido': TextInput(attrs={'class': 'form-control'}),
    # 'ci': TextInput(attrs={'class': 'form-control'}),
    # 'dir': TextInput(attrs={'class': 'form-control'}),
    # 'tel': TextInput(attrs={'class': 'form-control'}),
    # 'email': Ema(attrs={'class': 'form-control'}),
