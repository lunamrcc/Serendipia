from django.db import models

# Create your models here.
class Estudiantes(models.Model):

    EstudianteID = models.IntegerField(
        primary_key=True,
        null=False,

    )

    Nombre = models.CharField(
        max_length =50,
        null=False,
    )

    aPaterno = models.CharField(
        max_length=30,
        null=False,
    )
    aMaterno = models.CharField(
        max_length=30,
        null=False,
    )
    Telefono = models.CharField(
        max_length=15,
        null=False,
    )
    Escuela = models.CharField(
        max_length=50,
        null=False,
    )
    Correo = models.EmailField(
        null=False,
    )
    Passwd = models.CharField(
        max_length=20,
        null=False,
    )
    Activo = models.BooleanField(
        default = True,
    )

    def __str__(self):
        return self.Nombre +' '+ self.aPaterno +' '+ self.aMaterno