from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from biblioteca.views import (
	autor_add_api, autor_delete_api, autor_edit_api, autor_lista_api,
	libro_lista_api, libro_add_api, libro_edit_api, libro_delete_api)
from biblioteca.api import (
	autor_list_api, autor_detail_api, libro_list_api, libro_detail_api)

urlpatterns = [
    # Django REST Framework
    url(r'^api/autores/$', autor_list_api, name='api_autor'),
    url(r'^api/autores/(?P<pk>[0-9]+)/$', autor_detail_api, name='autor_detail_api'),

    url(r'^api/autores/lista/$', autor_lista_api, name='autor_lista_api'),
    url(r'^api/autores/agregar/$', autor_add_api, name='autor_add_api'),
    url(r'^api/autores/editar/(?P<id_autor>[0-9]+)/$', autor_edit_api, name='autor_edit_api'),
    url(r'^api/autores/eliminar/(?P<id_autor>[0-9]+)/$', autor_delete_api, name='autor_delete_api'),

    url(r'^api/libros/$', libro_list_api, name='libro_list_api'),
    url(r'^api/libros/(?P<pk>[0-9]+)/$', libro_detail_api, name='libro_detail_api'),

    url(r'^api/libros/lista/$', libro_lista_api, name='libro_lista_api'),
    url(r'^api/libros/agregar/$', libro_add_api, name='libro_add_api'),
    url(r'^api/libros/editar/(?P<id_libro>[0-9]+)/$', libro_edit_api, name='libro_edit_api'),
    url(r'^api/libros/eliminar/(?P<id_libro>[0-9]+)/$', libro_delete_api, name='libro_delete_api'),


    # My Olympia
    #url(r'^api/olympias/lista/$', mr_olympia_lista_api, name='mr_olympia_lista_api'),
    #url(r'^api/olympias/agregar/$', mr_olympia_add_api, name='mr_olympia_add_api'),
    
]