from django.shortcuts import render

def inicio(request):
    return render(request, 'AppCine/inicio.html')

def pelicula(request):
    return render(request, 'AppCine/peliculas.html')

def director(request):
    return render(request, 'AppCine/directores.html')

def guionista(request): 
    return render(request, 'AppCine/guionistas.html')

def actor(request):
    return render(request, 'AppCine/actores.html')