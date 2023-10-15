# Create your models here.
from django.db import models
from users.models import Renter
from vehicles.models import Vehicle

class Booking(models.Model):
    renter = models.ForeignKey(
        Renter,
        on_delete=models.CASCADE,
        related_name='reservas_realizadas',
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    create_add = models.DateField(auto_now=False, auto_now_add=False, null=True)
    # Otros campos como estado de reserva, precio, etc.
