from tkinter import Message
from django.shortcuts import get_object_or_404, render, redirect
from vehicles.models import Imagen, Vehicle, VehicleType, Location
from reviews.models import Review
from users.models import User, UserProfile, VehicleOwner
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


@login_required
def ultimos_4_vehicle_list(request):
    # Filtra los vehículos del usuario autenticado y obtén los últimos 4 registros
    user_vehicles = Vehicle.objects.filter(owner=request.user).order_by('-id')[:4]

    vehicle_types = VehicleType.objects.all()
    locations = Location.objects.all()

    context = {
        'user_vehicles': user_vehicles,
        'vehicle_types': vehicle_types,
        'locations': locations
    }

    return render(request, 'vehicle_list.html', context)

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
        transmision = request.POST['transmision']
        cilindraje = request.POST['cilindraje']
        descripcion = request.POST['descripcion']
        precio_por_hora = request.POST['precio_por_hora']
        precio_por_dia = request.POST['precio_por_dia']
        disponibilidad = request.POST.get('disponibilidad')
        disponibilidad = disponibilidad == 'on'
        combustible = request.POST['combustible']
        motor = request.POST['motor']
        tipo_freno = request.POST['tipo_freno']
        tipo_vehiculo = request.POST.get('tipo_vehiculo')
        location = request.POST.get('ubicacion')

        # Obtén el usuario autenticado
        user = request.user

        if user.is_owner:
            try:
                # Intenta obtener el VehicleOwner relacionado con el User
                vehicle_owner, created = VehicleOwner.objects.get_or_create(user=user)

                # Intenta obtener el objeto VehicleType correspondiente al ID proporcionado
                vehicle_type = VehicleType.objects.get(id=tipo_vehiculo)
                location = Location.objects.get(id=location)

                # Si se encontró un VehicleOwner y un VehicleType válido, procede a crear el vehículo
                vehicle = Vehicle(owner=vehicle_owner, vehicle_type=vehicle_type, location=location)
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
                imagenes = request.FILES.getlist('imagenes[]')
                for imagen in imagenes:
                    imagen_obj = Imagen(image=imagen, user=request.user)
                    imagen_obj.save()
                    vehicle.image.add(imagen_obj)
                    
                return redirect('vehicle_list')
            
            except VehicleType.DoesNotExist:
                # Si no se encontró un VehicleType correspondiente, muestra un mensaje de error
                Message.error(request, 'El tipo de vehículo seleccionado no es válido.')
                return redirect('become_owner')
        else:
            # Si el usuario no es propietario, redirige al usuario a la página de registro de propietario
            return redirect('become_owner')

    context = {
        'locations': locations,
        'vehicle_types': vehicle_types,
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





@login_required
def crear_vehiculo_paso1(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        anio = request.POST['anio']
        color = request.POST['color']
        puertas = request.POST['puertas']
        transmision = request.POST['transmision']
        cilindraje = request.POST['cilindraje']
        descripcion = request.POST['descripcion']

        datos_paso1 = {
            'marca': marca,
            'modelo': modelo,
            'anio': anio,
            'color': color,
            'puertas': puertas,
            'transmision': transmision,
            'cilindraje': cilindraje,
            'descripcion': descripcion,
        }

        request.session['datos_paso1'] = datos_paso1

        return redirect('crear_vehiculo_paso2')

    return render(request, 'crear_vehiculo_paso1.html')

@login_required
def crear_vehiculo_paso2(request):
    if request.method == 'POST':
        precio_por_hora = request.POST['precio_por_hora']
        precio_por_dia = request.POST['precio_por_dia']
        disponibilidad = request.POST.get('disponibilidad')
        combustible = request.POST['combustible']
        motor = request.POST['motor']
        climatizacion = request.POST['climatizacion']
        kilometraje = request.POST['kilometraje']
        tipo_freno = request.POST['tipo_freno']

        datos_paso1 = request.session.get('datos_paso1', {})

        datos_paso2 = {
            'precio_por_hora': precio_por_hora,
            'precio_por_dia': precio_por_dia,
            'disponibilidad': disponibilidad == 'on',
            'combustible': combustible,
            'motor': motor,
            'tipo_freno': tipo_freno,
            'climatizacion': climatizacion,
            'kilometraje': kilometraje,
        }

        datos_combinados = {**datos_paso1, **datos_paso2}
        request.session['datos_combinados'] = datos_combinados

        return redirect('crear_vehiculo_paso3')

    return render(request, 'crear_vehiculo_paso2.html')

@login_required
def crear_vehiculo_paso3(request):
    locations = Location.objects.all()
    vehicle_types = VehicleType.objects.all()
    
    if request.method == 'POST':
        datos_combinados = request.session.get('datos_combinados', {})

               # Obtén el propietario de vehículo (VehicleOwner) asociado con el usuario autenticado
        try:
            vehicle_owner = VehicleOwner.objects.get(user=request.user)
        except VehicleOwner.DoesNotExist:
            # Maneja el caso donde no existe un propietario de vehículo
            return redirect('become_owner')

        # Crea un nuevo vehículo con el propietario y otros datos
        vehicle = Vehicle(owner=vehicle_owner)
        vehicle.availability = datos_combinados.get('disponibilidad', False)
        vehicle.marca = datos_combinados.get('marca', '')
        vehicle.modelo = datos_combinados.get('modelo', '')
        vehicle.year = datos_combinados.get('anio', 0)
        vehicle.cilindraje = datos_combinados.get('cilindraje', 0)
        vehicle.descripcion = datos_combinados.get('descripcion', '')
        vehicle.price_hourly = datos_combinados.get('precio_por_hora', 0)
        vehicle.price_daily = datos_combinados.get('precio_por_dia', 0)
        # Otros campos según tus modelos

        try:
            tipo_vehiculo_id = request.POST.get('tipo_vehiculo')
            location_id = request.POST.get('ubicacion')

            vehicle_type = vehicle_types.get(id=tipo_vehiculo_id)
            location = locations.get(id=location_id)

            vehicle.vehicle_type = vehicle_type
            vehicle.location = location
            vehicle.save()

            imagenes = request.FILES.getlist('imagenes[]')

            for imagen in imagenes:
                imagen_obj = Imagen(image=imagen, user=request.user)
                imagen_obj.save()
                vehicle.image.add(imagen_obj)

            return redirect('vehicle_list')
        except (VehicleType.DoesNotExist, Location.DoesNotExist):
            return redirect('become_owner')

    return render(request, 'crear_vehiculo_paso3.html', {'locations': locations, 'vehicle_types': vehicle_types})