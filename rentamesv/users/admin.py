from django.contrib import admin
from .models import UserProfile, User, VehicleOwner, Renter, Review

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    
    pass
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(VehicleOwner)
class VehicleOwnerAdmin(admin.ModelAdmin):
    pass
@admin.register(Renter)
class RenterAdmin(admin.ModelAdmin):
    pass
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
