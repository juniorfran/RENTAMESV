from django.shortcuts import render
from vehicles.models import Vehicle, VehicleType, Location
from reviews.models import Review
from django.core.paginator import Paginator
from vehicles.models import Vehicle

def index (request):

    return render(request, 'base.html')

def your_view(request):
    is_home = request.path == 'home'
    return render(request, 'base.html', {'is_home': is_home})

def carrusel_view(request):
    image = Vehicle.objects.all()
    return render(request, 'carusel_view.html', {'image': image})