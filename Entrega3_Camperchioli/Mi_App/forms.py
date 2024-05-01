# En mi_app/forms.py

from django import forms
from .models import Clase1, Clase3

class Clase1Form(forms.ModelForm):
    class Meta:
        model = Clase1
        fields = ['campo1', 'campo2']

class Clase3Form(forms.ModelForm):
    class Meta:
        model = Clase3
        fields = ['campo4', 'campo5']
