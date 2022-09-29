from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.

def inicio(request):

    return render(request,"AppCoder/inicio.html")

def familia(request):

    fam1 = Familia(nombre="Marcelo", años= 64, fecha= "1957-12-15", familiar="padre")
    fam1.save()
    fam2 = Familia(nombre="Maria", años= 66, fecha= "1956-9-16", familiar="madre")
    fam2.save()
    fam3 = Familia(nombre="Fernanda", años= 22, fecha= "2000-7-14", familiar="hermana")
    fam3.save()


    return HttpResponse(f"Mi {fam1.familiar} se llama {fam1.nombre} tiene {fam1.años} y su nacimiento es el {fam1.fecha}. Mi {fam2.familiar} se llama {fam2.nombre} tiene {fam2.años} y su nacimiento es el {fam2.fecha}. Mi {fam3.familiar} se llama {fam3.nombre} tiene {fam3.años} y su nacimiento es el {fam3.fecha}.")

def estudiante(request):

    return render(request,"AppCoder/estudiantes.html")


def profesor(request):

    return render(request,"AppCoder/profesor.html")


def entregable(request):

    return render(request,"AppCoder/entregables.html")