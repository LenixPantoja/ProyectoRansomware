from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    contrasenia = models.TextField()
    numeroTC = models.TextField()
    ccv = models.TextField()
    fechaCaducidad = models.TextField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()