# Create your models here.
from autenticacion.models import Loggeable
from django.db import models


class Empresa(Loggeable):    
    nombre = models.CharField(max_length=150)
    
    def get_full_name(self):
        return f"Emp. nombre: {self.nombre} - email: {self.email}"
    
    def get_short_name(self):
        return self.nombre