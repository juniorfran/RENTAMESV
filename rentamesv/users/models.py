
# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='profile',
    )
    email = models.EmailField(max_length=254, null=True)
    numero_telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=150)
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    # Otros campos adicionales, como dirección, imagen de perfil, etc.

class User(AbstractUser):
    
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_users',  # Cambia este nombr{}
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='custom_users_permissions',  # Cambia este nombre
        related_query_name='custom_user_permission'
    )
    # Utilizamos el modelo AbstractUser de Django para la autenticación de usuarios
    # Puedes agregar campos adicionales si es necesario


class VehicleOwner(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='vehicle_owner_profile',
    )
    # Información de verificación
    id_document = models.CharField(max_length=20)  # Documento de identificación
    emergency_contact = models.CharField(max_length=100)  # Contacto de emergencia
    # Historial de alquiler de vehículos
    rented_vehicles = models.ManyToManyField('vehicles.Vehicle', blank=True, related_name='owners')
    # Preferencias de alquiler
    rental_price_hourly = models.DecimalField(max_digits=10, decimal_places=2)
    rental_price_daily = models.DecimalField(max_digits=10, decimal_places=2)
    availability_hours = models.CharField(max_length=100)  # Horarios disponibles
    rental_conditions = models.TextField()  # Condiciones de alquiler
    # Otros campos según tus necesidades

class Renter(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='renter_profile',
    )
    # Información de verificación
    id_document = models.CharField(max_length=20)  # Documento de identificación
    emergency_contact = models.CharField(max_length=100)  # Contacto de emergencia
    # Historial de alquiler de vehículos
    bookings = models.ManyToManyField('vehicles.Booking', blank=True, related_name='renters')
    # Preferencias de alquiler
    preferred_vehicle_types = models.ManyToManyField('vehicles.VehicleType', related_name='preferred_renters')
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    preferred_rental_dates = models.CharField(max_length=100)  # Fechas y horarios preferidos
    preferred_payment_methods = models.ManyToManyField('paymentmethod.PaymentMethod', related_name='preferred_pago_renters')
    required_documents = models.TextField()  # Documentos requeridos para alquilar
    driving_history = models.TextField()  # Historial de conducción
    # Otros campos según tus necesidades

class Review(models.Model):
    rating = models.PositiveIntegerField()  # Calificación (de 1 a 5)
    comment = models.TextField()  # Comentario
    date_added = models.DateTimeField(auto_now_add=True)  # Fecha de la valoración
    reviewed_by = models.ForeignKey('Renter', on_delete=models.CASCADE, related_name='reviews')
