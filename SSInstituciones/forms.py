from .models import SSInstituciones
from Instituciones.models import Instituciones
from django import forms

class InstForm(forms.ModelForm):
    class Meta:
        model = Instituciones
        fields = ('nombre', 'direccion', 'telefono', 'coordenadaX', 'coordenadaY',)