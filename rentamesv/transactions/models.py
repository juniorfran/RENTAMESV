from django.db import models
from users.models import Renter
from vehicles.models import Vehicle

class Transaction(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_add = models.DateField(auto_now=False, auto_now_add=False,  null=True)
    # Otros campos relacionados con la transacción
