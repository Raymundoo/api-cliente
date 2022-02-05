from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from api.views import (mr_olympia_lista_api)

urlpatterns = [
    # My Olympia
    url(r'^api/olympias/lista/$', mr_olympia_lista_api, name='mr_olympia_lista_api'),
    #url(r'^api/olympias/agregar/$', mr_olympia_add_api, name='mr_olympia_add_api'),
    
]