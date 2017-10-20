from django.conf.urls import url

from . import views

app_name = 'Estudiantes'

urlpatterns = [
    #administrador/estudiantes
    url(r'^$', views.student_lists, name='student_lists'),

    # administrador/estudiantes/3/delete
    url(r'^(?P<pk>[0-9]+)/eliminar/$', views.student_delete, name='student_delete'),

    # administrador/estudiantes/3/cambio_status
    url(r'^(?P<pk>[0-9]+)/cambio_status/$', views.student_change_status, name='student_change_status'),

    # administrador/usuarios_crear/
    url(r'^_crear/$', views.student_create, name='student_create'),
]