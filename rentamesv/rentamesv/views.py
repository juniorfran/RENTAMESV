from django.shortcuts import render
from vehicles.models import Vehicle, VehicleType, Location
from reviews.models import Review
from django.core.paginator import Paginator

def index (request):

    return render(request, 'base.html')