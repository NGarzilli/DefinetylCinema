from django.urls import path

from .views  import *

urlpatterns = [
       path('', inicio),
       path('peliculas', pelicula),
       path('directores', director),
       path('guionistas', guionista),
       path('actores', actor),
]