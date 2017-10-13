from django.db import models

# Create your models here.

class Usuarios(models.Model):

    Usuarioid = models.IntegerField(
        primary_key=True,
        null=False,
    )

    Nombre = models.CharField(
        max_length=50,
        null=False
    )

    Apaterno = models.CharField(
        max_length=50,
        null=False
    )

    Amaterno = models.CharField(
        max_length=50,
        null=False
    )

    Telefono = models.CharField(
        max_length=15,
    )

    Email = models.EmailField(
        null=False
    )

    Passwd = models.CharField(
        max_length=20,
        null=False
    )

    Activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.Nombre + ' ' + self.Apaterno + ' ' + self.Amaterno
