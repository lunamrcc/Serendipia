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

    # administrador/estudiantes/crear/
    url(r'^crear/$', views.student_create, name='student_create'),

    #administrador/estudiantes_editar/3
    url(r'^_editar/(?P<pk>[0-9]+)/', views.student_update.as_view(), name='student_update'),
]