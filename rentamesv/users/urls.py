from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import UserProfileViewSet, UserfileViewSet, VehicleOwnerViewSet, RenterViewSet, ReviewViewSet

# Crea un router
router = DefaultRouter()

# Registra la vista para el modelo UserProfile
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'user', UserfileViewSet)
router.register(r'vehicleowner', VehicleOwnerViewSet)
router.register(r'renter', RenterViewSet)
router.register(r'review', ReviewViewSet)




urlpatterns = [
    # Otras rutas de la aplicación
    path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('crear_perfil/', views.crear_perfil, name='crear_perfil'),
    path('perfil/', views.profileView, name='perfil'),
    path('become_owner/', views.become_owner, name='become_owner'),
    path('complete_verification/', views.complete_verification, name='complete_verification'),
    
    
    
    ##API RUTES
    path('api/', include(router.urls)),
    
    
]