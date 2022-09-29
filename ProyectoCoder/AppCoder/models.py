import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre = models.CharField(max_length=60)
    años = models.IntegerField()
    fecha = models.DateField()
    familiar = models.CharField(max_length=60)

class Estudiante(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()

class Profesor(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)

class Entregable(models.Model):

    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()


