from multiprocessing import AuthenticationError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth.models import User
from .models import UserProfile, VehicleOwner, Renter, User
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

#VISTA DE REGISTRARSE CON EL USUARIO Y LA CLAVE QUE SE LE ASIGNE A TRAVES


#VISTA PARA VER EL PERFIL DEL USUARIO
@login_required
def profileView(request):
    user = request.user

    # Verificar si el usuario tiene un perfil
    if not UserProfile.objects.filter(user=user).exists():
        return redirect('crear_perfil')  # Redireccionar a la vista de creación de perfil

    # El usuario tiene un perfil, obtén los datos del perfil
    perfil = user.profile
    full_name = user.get_full_name()
    email = user.email
    vehicles = Vehicle.objects.filter(owner__user=user)

    context = {
        'perfil': perfil,
        'full_name': full_name,
        'email': email,
        'vehicles': vehicles,
    }

    return render(request, 'perfil/perfil.html', context)

#VISTA PARA REGISTRAR USUARIO SIN ARCHIVO FORM
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validar que las contraseñas coincidan
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('home')

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('home')

        # Crear el nuevo usuario
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('home')

    return render(request, 'users/register.html')


## VISTA PARA REGISTRAR UN PERFIL
@login_required
def crear_perfil(request):
        # Verificar si el usuario ya tiene un perfil
    if UserProfile.objects.filter(user=request.user).exists():
        return redirect('perfil')

    if request.method == 'POST':
        # Obtén el usuario actualmente autenticado
        user = request.user
        email = request.user.email

        # Obtén los datos del formulario
        # email = request.POST['email']
        numero_telefono = request.POST['numero_telefono']
        direccion = request.POST['direccion']
        nombre = request.POST['nombre']
        imagen = request.FILES.get('imagen')  # campo de archivo para la imagen

        # Crea el objeto UserProfile relacionado con el usuario autenticado
        perfil_usuario, creado = UserProfile.objects.get_or_create(user=user)
        perfil_usuario.email = email
        perfil_usuario.numero_telefono = numero_telefono
        perfil_usuario.direccion = direccion
        perfil_usuario.nombre = nombre
        if imagen:
            perfil_usuario.imagen = imagen
        perfil_usuario.save()

        # Redirecciona a la página de perfil del usuario
        return redirect('perfil')

    return render(request, 'perfil/crear_perfil.html')


#VISTA PARA HACER LOGIN BASADA EN FUNCION SIN ARCHIVOS FORM
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('crear_perfil')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return redirect('home')

    return render(request, 'users/login.html')

##VISTA DE LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with your desired redirect URL

## VISTA PARA VER LA CANTIDAD DE vehicle QUE ESTAN RELACIONADOS AL USUARIO
# @login_required
# def vervehiculos(request):
#     if (request.user != None and request.user.is_authenticated()):
        
@login_required
def become_owner(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        user_profile.is_owner = True
        user_profile.save()
        return redirect('complete_verification')  # Redirige a la página de verificación

    return render(request, 'owner/become_owner.html')


# Vista para completar la información de verificación
@login_required
def complete_verification(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Procesa el formulario de información de verificación
        id_document = request.POST.get('id_document')
        emergency_contact = request.POST.get('emergency_contact')
        rental_price_hourly = request.POST.get('rental_price_hourly')
        rental_price_daily = request.POST.get('rental_price_daily')
        availability_hours = request.POST.get('availability_hours')
        rental_conditions = request.POST.get('rental_conditions')
        
        # Procesa las imágenes adjuntas si se proporcionan
        foto1_dui = request.FILES.get('foto1_dui')
        foto2_dui = request.FILES.get('foto2_dui')
        foto_licencia = request.FILES.get('foto_licencia')

        # Crea un objeto VehicleOwner relacionado con el perfil de usuario
        vehicle_owner, created = VehicleOwner.objects.get_or_create(user=user_profile.user)
        vehicle_owner.id_document = id_document
        vehicle_owner.emergency_contact = emergency_contact
        vehicle_owner.rental_price_hourly = rental_price_hourly
        vehicle_owner.rental_price_daily = rental_price_daily
        vehicle_owner.availability_hours = availability_hours
        vehicle_owner.rental_conditions = rental_conditions

        # Asigna las imágenes si se proporcionan
        if foto1_dui:
            vehicle_owner.foto1_dui = foto1_dui
        if foto2_dui:
            vehicle_owner.foto2_dui = foto2_dui
        if foto_licencia:
            vehicle_owner.foto_licencia = foto_licencia

        vehicle_owner.save()

        return redirect('dashboard')  # Redirige al panel de control

    return render(request, 'owner/complete_verification.html')

