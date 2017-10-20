from .models import Usuarios
from django import forms

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('Nombre', 'Apaterno', 'Amaterno', 'Telefono', 'Email', 'Passwd')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        passwd = forms.CharField(widget=forms.PasswordInput)
        fields = ('Email', 'passwd')