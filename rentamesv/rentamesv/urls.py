
from django import views
from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import include, path
#from django.contrib.auth.models import User
from users.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    
    path('', views.index, name='home'),
    #path('lista_vehiculos/', views.vehicle_list, name='lista_vehiculos'),
    
    #url api
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    #urls de users
    path('users/', include('users.urls')),
    
    
    #urls de vehicles
    path('vehicles/', include('vehicles.urls'))
    
    
]
