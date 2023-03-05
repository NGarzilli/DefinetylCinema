from django.shortcuts import render
from django.http  import HttpResponse

from AppCine.models import Pelicula

def pelicula(request):
    pelicula  =  Pelicula(nombre='The Thing', agno = '1982', genero= 'Terror/Ciencia ficcion')
    pelicula.save()
    respuesta=  f'Pelicula: {pelicula.nombre}, Año: {pelicula.agno}, Genero: {pelicula.genero}'

    return  HttpResponse(respuesta)