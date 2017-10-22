from django.db import models

# Create your models here.

class SSInstituciones(models.Model):
    institucionID = models.IntegerField(
        primary_key = True,
        null = False
    )
    nombre = models.CharField(
        max_length = 50,
        null = False
    )
    direccion = models.CharField(
        max_length = 50,
        null = False
    )
    telefono = models.CharField(
        max_length = 50,
        null = False
    )
    coordenadaX = models.FloatField(
        null = True
    )
    coordenadaY = models.FloatField(
        null = True
    )

    def __str__(self):
        return self.nombre

