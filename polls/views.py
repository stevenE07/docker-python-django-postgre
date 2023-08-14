from django.http import HttpResponse
from polls.models import Persona
# Create your views here.
def index(request):
    #insertar un elemento en la base de datos
    persona = Persona(nombre="Juan", apellido="Perez", edad=20, sexo="M", email='mail@prueba.com')
    persona.save()
    return HttpResponse("Hello, world. You're at the polls index.")