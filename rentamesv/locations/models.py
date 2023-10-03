from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)  # Nombre de la ubicación
    address = models.CharField(max_length=200)  # Dirección de la ubicación
    latitude = models.DecimalField(max_digits=10, decimal_places=6)  # Latitud
    longitude = models.DecimalField(max_digits=10, decimal_places=6)  # Longitud
