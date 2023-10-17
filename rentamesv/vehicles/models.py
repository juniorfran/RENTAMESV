from django.db import models
from users.models import Renter

def vehicle_directory_path(instance, filename):
    # instance es el modelo UserProfile al que se adjuntará la imagen
    # filename es el nombre del archivo original

    # Obtén el nombre de usuario del usuario al que pertenece la instancia
    username = instance.user.username

    # Define la ruta donde se guardarán las imágenes
    # En este ejemplo, se guardarán en una carpeta con el nombre del usuario dentro de 'profile_images/'
    return f'vehicle_images/user_{username}/{filename}'

class Vehicle(models.Model):
    make = models.CharField(max_length=50)  # Marca del vehículo
    model = models.CharField(max_length=50)  # Modelo del vehículo
    year = models.PositiveIntegerField()  # Año del vehículo
    vehicle_type = models.ForeignKey('VehicleType', on_delete=models.CASCADE)  # Tipo de vehículo
    description = models.TextField()  # Descripción del vehículo  
    image = models.ManyToManyField('Imagen', blank=True) # Imagen del vehículo
    price_hourly = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por hora
    price_daily = models.DecimalField(max_digits=10, decimal_places=2)  # Precio por día
    availability = models.BooleanField(default=True)  # Disponibilidad del vehículo
    location = models.ForeignKey('Location', on_delete=models.CASCADE)  # Ubicación del vehículo
    owner = models.ForeignKey('users.VehicleOwner', on_delete=models.CASCADE, related_name='owned_vehicles')
    reviews = models.ManyToManyField('users.Review', blank=True, related_name='reviewed_vehicles')
    color = models.CharField(max_length=50, null=True)
    puertas = models.CharField(max_length=50, null=True)
    capacidad = models.CharField(max_length=50, null=True)
    combustible = models.CharField(max_length=50, null=True)
    motor = models.CharField(max_length=50, null=True)
    tipo_freno = models.CharField(max_length=50, null=True)
    create_add = models.DateField(auto_now=True, auto_now_add=False, null=True)
    foto_tarjeta_circulacion_1 = models.FileField( upload_to=vehicle_directory_path, max_length=100, null=True)
    foto_tarjeta_circulacion_2 = models.FileField( upload_to=vehicle_directory_path, max_length=100, null=True)
    
# class seguro_vehiculo(models.model):
#     create_add = models.DateField(auto_now=False, auto_now_add=False, null=True)
#     user = models.ForeignKey('users.User', on_delete=models.CASCADE)
#     vehiculo = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    
    
    
class Imagen(models.Model):
    image = models.ImageField(upload_to=vehicle_directory_path)
    create_add = models.DateField(auto_now=False, auto_now_add=False, null=True)

class VehicleType(models.Model):
    name = models.CharField(max_length=50)
    capacidad = models.CharField(max_length=50, null=True)
    create_add = models.DateField(auto_now=False, auto_now_add=False, null=True)

class Location(models.Model):
    name = models.CharField(max_length=100)  # Nombre de la ubicación
    address = models.CharField(max_length=200)  # Dirección de la ubicación
    latitude = models.DecimalField(max_digits=10, decimal_places=6)  # Latitud
    longitude = models.DecimalField(max_digits=10, decimal_places=6)  # Longitud
    create_add = models.DateField(auto_now=False, auto_now_add=False,  null=True)

class Booking(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='reservas')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    create_add = models.DateField(auto_now=False, auto_now_add=False,  null=True)
    # Otros campos como estado de reserva, precio, etc.
