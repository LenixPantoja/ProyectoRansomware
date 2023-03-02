from django.shortcuts import render, HttpResponseRedirect
from .models import Persona
# Create your views here.

def registroDatos(request):
    if request.method == 'POST':
        persona = Persona(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            correo = request.POST['correo'],
            contrasenia = request.POST['contrasenia'],
            numeroTC = request.POST['numeroTC'],
            ccv = request.POST['ccv'],
            fechaCaducidad = request.POST['fechaCaducidad'],
            telefono=request.POST['telefono'],
            direccion = request.POST['direccion']
        )
        persona.save()
        return HttpResponseRedirect('/key/')
    else:
        return render(request, 'registro.html')
    
def obtener_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

def mostrarKey(request):
    return render(request, 'clave.html')