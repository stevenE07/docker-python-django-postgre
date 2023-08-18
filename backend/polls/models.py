from django.db import models

# Create your models here.

from django.db import models

class Persona(models.Model):
    email = models.CharField(max_length=100, unique=True)
    contrasenia = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=1)

    def __str__(self):
        return f"[Persona] nombre: '{self.nombre}'; apellido: '{self.apellido}'; edad: '{self.edad}'; sexo: '{self.sexo}'; email: '{self.email}'; contrasenia: '{self.contrasenia}'"
