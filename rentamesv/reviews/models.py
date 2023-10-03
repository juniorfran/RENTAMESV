from django.db import models
from users.models import Renter

class Review(models.Model):
    rating = models.PositiveIntegerField()  # Calificación (de 1 a 5)
    comment = models.TextField()  # Comentario
    date_added = models.DateTimeField(auto_now_add=True)  # Fecha de la valoración
    reviewed_by = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='reviews')
