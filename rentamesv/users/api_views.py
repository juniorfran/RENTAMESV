from rest_framework import viewsets
from .models import UserProfile, User, VehicleOwner, Renter, Review
from .serializers import UserProfileSerializer, UserfileSerializer, VehicleOwnerSerializer, RenterSerializer, ReviewSerializer  # Asegúrate de importar el serializador adecuado

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class UserfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserfileSerializer

class VehicleOwnerViewSet(viewsets.ModelViewSet):
    queryset = VehicleOwner.objects.all()
    serializer_class = VehicleOwnerSerializer

class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    