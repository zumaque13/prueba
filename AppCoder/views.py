from django.http import HttpResponse
from django.shortcuts import render

from AppCoder.models import Curso

# Create your views here.

def crea_curso(self, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)

    curso.save()

    return HttpResponse (f'Se creo un nuevo curso de nombre {curso.nombre} con el nro camada {curso.camada}')