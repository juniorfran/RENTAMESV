from django.contrib import admin
from .models import Vehicle, VehicleType, Location, Booking

# Register your models here.

#agregar vehiculo a el admin
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'vehicle_type', 'price_hourly', 'price_daily', 'availability')
    list_filter = ('make', 'model', 'year', 'vehicle_type', 'availability')
    search_fields = ('make', 'model', 'year')
    
@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('renter', 'vehicle', 'start_date', 'end_date')
    

