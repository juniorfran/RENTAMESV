from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # Otras rutas URL aquí, si las tienes.
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
    
    ## URL PARA VEHICULO RELACIONADA AL USUARIO
    path("create_user_vehicle/", views.crear_vehiculo, name="create_user_vehicle"),
    
    
    path('crear_vehiculo/paso1/', views.crear_vehiculo_paso1, name='crear_vehiculo_paso1'),
    path('crear_vehiculo/paso2/', views.crear_vehiculo_paso2, name='crear_vehiculo_paso2'),
    path('crear_vehiculo/paso3/', views.crear_vehiculo_paso3, name='crear_vehiculo_paso3'),
]

# Configuración de las rutas de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
