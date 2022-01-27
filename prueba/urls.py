from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from biblioteca import views
from contactos.views  import contactos
from pokemon.views  import get_pokemon,info_pokemon,tipo_pokemon

"""

aumento 
xd
"""
urlpatterns = [
    
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
    url(r'^$', views.LibrosList.as_view(),name='libro_lista'),
    url(r'^nuevo/$', views.LibroCreate.as_view(),name='libro_nuevo'),
    url(r'^editar/(?P<pk>\d+)/$', views.LibroUpdate.as_view(),name='libro_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', views.LibroDelete.as_view(),name='libro_eliminar'),
    url(r'^func/lista/$', views.libro_list,name='libro_funct_lista'),
    url(r'^func/nuevo/$', views.libro_add,name='libro_funct_nuevo'),
    url(r'^funct/editar/(?P<id_libro>\d+)/$', views.libro_edit,name='libro_funct_editar'),
    url(r'^funct/eliminar/(?P<id_libro>\d+)/$', views.libro_delete,name='libro_funct_eliminar'),
    # ---------------- Autor-----------------------------------------------
    url(r'^autor/lista/$', views.AutorList.as_view(),name='autor_lista'),
    url(r'^autor/nuevo/$', views.AutorCreate.as_view(),name='autor_nuevo'),
    url(r'^autor/editar/(?P<pk>\d+)/$', views.AutorUpdate.as_view(),name='autor_editar'),
    url(r'^autor/eliminar/(?P<pk>\d+)/$', views.AutorDelete.as_view(),name='autor_eliminar'),
    url(r'^autor/func/lista/$', views.autor_list,name='autor_funct_lista'),
    url(r'^autor/func/nuevo/$', views.autor_add,name='autor_funct_nuevo'),
    url(r'^autor/func/editar/(?P<id_autor>\d+)/$', views.autor_edit,name='autor_funct_editar'),
    url(r'^autor/func/eliminar/(?P<id_autor>\d+)/$', views.autor_delete,name='autor_funct_eliminar'),
    url(r'^contactos/$', contactos),
    # ---------------- pokemon-----------------------------------------------
    url(r'^pokemon/$', get_pokemon,name='index_pokemon'),
    url(r'^pokemon/detalle/(?P<id_pokemon>\d+)/$',info_pokemon,name='detalle_pokemon'),
    url(r'^pokemon/tipo/(?P<id_tipo>\d+)/$',tipo_pokemon,name='tipo_pokemon'),

    url(r'^', include('biblioteca.urls')),
]
