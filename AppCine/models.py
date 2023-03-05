from django.db import models

class Pelicula(models.Model):
    
    nombre = models.CharField(max_length=60)
    agno = models.IntegerField()
    genero = models.CharField(max_length=30)

class Director(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Guionista(models.Model):
   
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class Actor(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50) 