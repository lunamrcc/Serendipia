from .models import Usuarios
from django import forms

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('Nombre', 'Apaterno', 'Amaterno', 'Telefono', 'Email', 'Passwd')