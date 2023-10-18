from django.shortcuts import render, redirect
from vehicles.models import Imagen, Vehicle, VehicleType, Location
from reviews.models import Review
from users.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.order_by('-id')  # Ordena la lista de vehículos por fecha de creación en orden descendente
    vehicle_types = VehicleType.objects.all()
    locations = Location.objects.all()
    
    paginator = Paginator(vehicles, 10)  # Configurar el paginador con 10 elementos por página
    page = request.GET.get('page')
    
    try:
        vehicles = paginator.page(page)  # Obtener la página específica
    except PageNotAnInteger:
        # Si la página no es un número entero, mostrar la primera página.
        vehicles = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango (por encima del número máximo de páginas), mostrar la última página.
        vehicles = paginator.page(paginator.num_pages)
    
    context = {
        'vehicles': vehicles,
        'vehicle_types': vehicle_types,
        'locations': locations
    }
    
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
        vehicle.description = descripcion
        vehicle.price_hourly = precio_por_hora
        vehicle.price_daily = precio_por_dia
        vehicle.availability = disponibilidad
        vehicle.combustible = combustible
        vehicle.motor = motor
        vehicle.tipo_freno = tipo_freno
        vehicle.save()

        # Procesa las imágenes
        imagenes = request.FILES.getlist('imagenes[]')  # Obtiene una lista de archivos
        for imagen in imagenes:
            imagen_obj = Imagen(image=imagen)
            imagen_obj.save()
            vehicle.image.add(imagen_obj)

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