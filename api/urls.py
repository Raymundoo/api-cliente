from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from api.views import (mascota_lista_api, mr_olympia_lista_api, mascota_lista_api_token)

urlpatterns = [
    # My Olympia
    url(r'^api/olympias/lista/$', mr_olympia_lista_api, name='mr_olympia_lista_api'),
    #url(r'^api/olympias/agregar/$', mr_olympia_add_api, name='mr_olympia_add_api'),
    
    # Mascotas
    url(r'^api/mascotas/lista/$', mascota_lista_api, name='mascota_lista_api'),
    url(r'^api/mascotas/lista/token/$', mascota_lista_api_token, name='mascota_lista_api_token'),
]