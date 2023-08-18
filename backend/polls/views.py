import json
from django.http import HttpResponse, HttpRequest
from polls.models import Persona
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    #insertar un elemento en la base de datos
    persona = Persona(nombre="lucio", apellido="Perez", edad=20, sexo="M", email='lucio@prueba.com', contrasenia='1234')
    persona.save()
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def authenticate(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        
        headers = {
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        try:
            persona = Persona.objects.get(email__contains=json_data['email'])
            json_response = str(persona)
            return HttpResponse({}, status=200, headers=headers)
        except Persona.DoesNotExist:
            return HttpResponse("Person not found", status=404, headers=headers)

    return HttpResponse("Invalid request method", status=405)
