from django.db import models

class Usuario(models.Model):
    dni = models.IntegerField(max_length=8)
    cuenta = models.CharField(max_length=200)
    contraseña = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)