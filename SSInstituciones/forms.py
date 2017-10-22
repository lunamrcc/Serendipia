from .models import SSInstituciones
from django import forms

class InstForm(forms.ModelForm):
    class Meta:
        model = SSInstituciones
        fields = ('nombre', 'direccion', 'telefono', 'coordenadaX', 'coordenadaY',)