from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio), 
    path("familia/", familia),
    path("profesores/", profesor),
    path("estudiantes/", estudiante),
    path("entregables/", entregable),
]
