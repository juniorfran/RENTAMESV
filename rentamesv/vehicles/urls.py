from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Otras rutas URL aquí, si las tienes.
    path('vehicle_list/', views.vehicle_list, name='vehicle_list'),
]

# Configuración de las rutas de medios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
