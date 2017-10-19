from django.conf.urls import url, include
from Usuarios import urls
from . import views

app_name = 'Index'

urlpatterns = [

    #/administrador/
    url(r'^$', views.Index, name='dashboard'),

]