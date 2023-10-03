# Create your models here.
from django.db import models
from users.models import Renter
from vehicles.models import Vehicle

class Booking(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='bookings_made')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # Otros campos como estado de reserva, precio, etc.
