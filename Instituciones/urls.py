from django.conf.urls import url

from . import views

app_name = 'Instituciones'

urlpatterns = [
    #administrador/instituciones
    url(r'^$', views.inst_lists, name='inst_lists'),

    #administrador/instituciones/3/delete
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.inst_delete, name='inst_delete'),

    # administrador/instituciones/crear
    url(r'^crear/$', views.inst_create, name='inst_create'),

    # administrador/inst_editar/3
    url(r'^_editar/(?P<pk>[0-9]+)/', views.inst_update.as_view(), name='inst_update')

]