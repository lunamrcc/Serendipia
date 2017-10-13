from django.db import models

# Create your models here.

class Instituciones(models.Model):
    InstitucionID = models.IntegerField(
        primary_key = True,
        null = False
    )
    Nombre = models.CharField(
        max_length = 50,
        null = False
    )
    Direccion = models.CharField(
        max_length = 50,
        null = False
    )
    Telefono = models.CharField(
        max_length = 50,
        null = False
    )
    CoordenadaX = models.FloatField(
        null = True
    )
    CoordenadaY = models.FloatField(
        null = True
    )

    def __str__(self):
        return self.Nombre

