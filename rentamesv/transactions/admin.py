from django.contrib import admin
from .models import Transaction

# Register your models here.

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('renter', 'vehicle', 'transaction_date', 'amount')
    