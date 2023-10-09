from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas de la aplicación
    path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]