from django.shortcuts import render
from django.http import HttpResponse # Creación de la clase que permite ejecutar una respuesta http

def index(request):
    return HttpResponse("Hello World")
