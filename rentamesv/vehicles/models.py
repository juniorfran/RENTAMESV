from django.db import models
from users.models import Renter

class Vehicle(models.Model):
    make = models.CharField(max_length=50)  # Marca del vehículo
    model = models.CharField(max_length=50)  # Modelo del vehículo
    year = models.PositiveIntegerField()  # Año del vehículo
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)  # Tipo de vehículo
    description = models.TextField()  # Descripción del vehículo
    image = models.ImageField(upload_to='vehicle_images/')  # Imagen del vehículo
    price_hourly = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por hora
    price_daily = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por día
    availability = models.BooleanField(default=True)  # Disponibilidad del vehículo
    location = models.ForeignKey('Location', on_delete=models.CASCADE)  # Ubicación del vehículo
    owner = models.ForeignKey('users.VehicleOwner', on_delete=models.CASCADE, related_name='owned_vehicles')
    reviews = models.ManyToManyField('users.Review', blank=True, related_name='reviewed_vehicles')

class VehicleType(models.Model):
    name = models.CharField(max_length=50)

class Location(models.Model):
    name = models.CharField(max_length=100)  # Nombre de la ubicación
    address = models.CharField(max_length=200)  # Dirección de la ubicación
    latitude = models.DecimalField(max_digits=10, decimal_places=6)  # Latitud
    longitude = models.DecimalField(max_digits=10, decimal_places=6)  # Longitud

class Booking(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='bookings')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # Otros campos como estado de reserva, precio, etc.
