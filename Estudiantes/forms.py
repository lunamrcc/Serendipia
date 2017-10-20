from .models import Estudiantes
from django import forms


class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ('Nombre', 'aPaterno', 'aMaterno', 'Telefono','Escuela', 'Correo', )
