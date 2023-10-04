from django.shortcuts import render
from vehicles.models import Vehicle, VehicleType, Location
from reviews.models import Review
from django.core.paginator import Paginator

def vehicle_list(request):
    # Obtén todos los vehículos disponibles
    vehicles = Vehicle.objects.filter(availability=True)

    # Aplica filtros si se proporcionan en la solicitud
    location = request.GET.get('location')
    make = request.GET.get('make')
    model = request.GET.get('model')
    year = request.GET.get('year')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if location:
        vehicles = vehicles.filter(location__name=location)
    if make:
        vehicles = vehicles.filter(make=make)
    if model:
        vehicles = vehicles.filter(model=model)
    if year:
        vehicles = vehicles.filter(year=year)
    # Agrega aquí la lógica para filtrar por rango de fechas (start_date y end_date)
    #LOGICA PARA FILTRAR POR RANGO DE FECHAS
    if start_date and not end_date:
        vehicles = vehicles.filter(start_date__gte=start_date)
    if end_date and not start_date:
        vehicles = vehicles.filter(end_date__lte=end_date)
    if start_date and end_date:
        vehicles = vehicles.filter(start_date__gte=start_date, end_date__lte=end_date)
        # Ordena los resultados en función del parámetro order
    if 'order' in request.GET:
        if request.GET['order'] == 'asc':
            vehicles = vehicles.order_by('price_hourly')
        if request.GET['order'] == 'desc':
            vehicles = vehicles.order_by('-price_hourly')
            paginator = Paginator(vehicles, 10)# Cantidad máxima de elementos que aparecen en cada página
            page_number = request.GET.get('page')
            page_vehicles = paginator.get_page(page_number)
            return render(request, 'lista_vehiculos.html', {'vehicles': page_vehicles})
    else:
        vehicles = vehicles.order_by('price_hourly')
        # Configura la paginación con 25 vehículos por página
        paginator = Paginator(vehicles, 25)
        page_number = request.GET.get('page')
        page_vehicles = paginator.get_page(page_number)

        return render(request, 'lista_vehiculos.html', {'vehicles': page_vehicles})

def index (request):

    return render(request, 'base.html')