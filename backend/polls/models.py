from django.db import models

# Create your models here.

from django.db import models

class Persona(models.Model):
    email = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
