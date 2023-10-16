from django.shortcuts import render, redirect
from vehicles.models import Vehicle, VehicleType, Location
from reviews.models import Review
from users.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.

@login_required
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

##VISTA PARA CREAR VEHICULOS RELACIONADO AL USUARIO LOGUEADO
@login_required
def crear_vehiculo(request):
    # Mueve la definición de las listas locations y vehicle_types aquí para que estén disponibles en el alcance de la vista
    locations = Location.objects.all()
    vehicle_types = VehicleType.objects.all()

    if request.method == 'POST':
        # Obtén los datos del formulario
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anio = request.POST['anio']
        color = request.POST['color']
        puertas = request.POST['puertas']
        transmision = request.POST['transmision']  # Agrega este campo
        cilindraje = request.POST['cilindraje']
        imagen = request.FILES.get('imagen')  # Campo de archivo para la imagen
        descripcion = request.POST['descripcion']  # Agrega este campo
        precio_por_hora = request.POST['precio_por_hora']  # Agrega este campo
        precio_por_dia = request.POST['precio_por_dia']  # Agrega este campo
        disponibilidad = request.POST.get('disponibilidad')  # Agrega este campo
        combustible = request.POST['combustible']  # Agrega este campo
        motor = request.POST['motor']  # Agrega este campo
        tipo_freno = request.POST['tipo_freno']  # Agrega este campo

        # Obtén el usuario autenticado
        user = request.user

        # Crea un objeto Vehicle relacionado con el usuario autenticado
        vehicle, creado = Vehicle.objects.get_or_create(owner=user)
        vehicle.make = marca
        vehicle.model = modelo
        vehicle.year = anio
        vehicle.color = color
        vehicle.puertas = puertas
        vehicle.transmision = transmision
        vehicle.cilindraje = cilindraje
        vehicle.image = imagen
        vehicle.location_id = request.POST['location']  # Asegúrate de obtener la ubicación correctamente
        vehicle.vehicle_type_id = request.POST['tipo_vehiculo']  # Asegúrate de obtener el tipo de vehículo correctamente
        vehicle.description = descripcion
        vehicle.price_hourly = precio_por_hora
        vehicle.price_daily = precio_por_dia
        vehicle.availability = disponibilidad
        vehicle.combustible = combustible
        vehicle.motor = motor
        vehicle.tipo_freno = tipo_freno
        vehicle.save()

        return redirect('vehicle_user_list')
        
    context = {
        'locations': locations,
        'vehicle_types': vehicle_types
    }

    return render(request, 'user/vehicle_user_create.html', context)


# class VehicleCreateView(LoginRequiredMixin, CreateView):
#     model = Vehicle
#     template_name = 'crear_vehiculo.html'  # Reemplaza con la ruta a tu plantilla HTML
#     fields = ['make', 'model', 'year', 'vehicle_type', 'description', 'image', 'price_hourly', 'price_daily', 'availability', 'location', 'color', 'puertas', 'capacidad', 'combustible', 'motor', 'tipo_freno']

#     def form_valid(self, form):
#         # Asigna el propietario del vehículo como el usuario autenticado
#         form.instance.owner = self.request.user.vehicleowner
#         return super().form_valid(form)

#     success_url = reverse_lazy('nombre_de_la_url_a_la_que_redireccionar_despues_de_guardar')