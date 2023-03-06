from django.contrib import admin
from django.urls import path, include

#from AppCine.views import pelicula

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppCine.urls'),)
]
