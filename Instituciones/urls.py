from django.conf.urls import url

from . import views

app_name = 'Instituciones'

urlpatterns = [
    #administrador/instituciones
    url(r'^$', views.inst_lists, name='inst_lists'),

    #administrador/usuarios/3/delete
    url(r'^/(?P<pk>[0-9]+)/eliminar/$', views.inst_delete, name='inst_delete'),

    # administrador/usuarios_crear/
    url(r'^_crear/$', views.inst_create, name='inst_create'),

]