from multiprocessing import AuthenticationError
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

#VISTA DE REGISTRARSE CON EL USUARIO Y LA CLAVE QUE SE LE ASIGNE A TRAVES
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        numero_telefono = request.POST['numero_telefono']
        direccion = request.POST['direccion']
        nombre = request.POST['nombre']
        email = request.POST['email']
        
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            # Comprueba si el usuario ya existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
            else:
                # Crea un nuevo usuario
                user = User.objects.create_user(username=username, password=password1)
                
                # Crea el perfil del usuario
                profile = UserProfile(user=username, numero_telefono=numero_telefono, direccion=direccion, nombre=nombre, email=email)
                profile.save()
                
                login(request, user)
                messages.success(request, 'Registro exitoso. Ahora estás conectado.')
                return redirect('Home')  # Reemplaza 'nombre_de_la_pagina_principal' por la URL de tu página principal.
    
    return render(request, 'users/register.html')

#VISTA PARA HACER LOGIN BASADA EN FUNCION SIN ARCHIVOS FORM
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso.')
            return redirect('home')  # Reemplaza 'nombre_de_la_pagina_principal' por la URL de tu página principal.
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'users/login.html')


##VISTA DE LOGOUT
def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with your desired redirect URL
