from django.conf.urls import url

from . import views

app_name = 'Usuarios'

urlpatterns = [
    #administrador/usuarios
    url(r'^$', views.user_lists, name='user_lists'),

    #administrador/usuarios/3/delete
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.user_delete, name='user_delete'),

    #administrador/usuarios/3/cambio_status
    url(r'^(?P<pk>[0-9]+)/cambio_status/$', views.user_change_status, name='user_change_status'),

    #administrador/usuarios_crear/
    url(r'^_crear/$', views.user_create, name='user_create'),

    #administrador/usuarios_editar/3
    url(r'^_editar/(?P<pk>[0-9]+)/', views.user_update.as_view(), name='user_update'),
]