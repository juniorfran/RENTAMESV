from django.shortcuts import render
from vehicles.models import Vehicle, VehicleType, Location
from reviews.models import Review
from django.core.paginator import Paginator

# Create your views here.


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    vehicle_types = VehicleType.objects.all()
    locations = Location.objects.all()
    
    context = {
        'vehicles': vehicles,
        'vehicle_types': vehicle_types,
        'locations': locations
    }
    
    paginator = Paginator(vehicles, 10)
    page = request.GET.get('page')
    vehicles = paginator.get_page(page)
    
    return render(request, 'vehicle_list.html', context)
