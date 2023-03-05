from django.contrib import admin
from django.urls import path

from AppCine.views  import pelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pelicula),
]
