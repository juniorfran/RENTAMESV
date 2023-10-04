from django.contrib import admin
from .models import PaymentMethod, CreditCardPayment, PayPalPayment, BankTransferPayment

# Register your models here.
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'created_at', 'updated_at')

@admin.register(CreditCardPayment)
class CreditCardPaymentAdmin(admin.ModelAdmin):
    list_display = ('cardholder_name', 'card_number', 'expiration_date', 'cvv', 'transaction')

@admin.register(PayPalPayment)
class PayPalPaymentAdmin(admin.ModelAdmin):
    list_display = ('email', 'transaction')

@admin.register(BankTransferPayment)
class BankTransferPaymentAdmin(admin.ModelAdmin):
    list_display = ('account_holder', 'account_number', 'bank_name', 'transaction')
    
    