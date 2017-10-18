from .models import Usuarios
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def user_lists(request):
    all_users = Usuarios.objects.all()
    context ={
        'all_users': all_users
        }
    return render(request, 'Usuarios/usuarios_list.html',context)

def user_delete(request, pk):
    user = Usuarios.objects.filter(Usuarioid=pk)
    user.delete()
    return HttpResponseRedirect(reverse('Usuarios:user_lists'))

def user_change_status(request, pk):
    user = Usuarios.objects.get(Usuarioid=pk)
    if user.Activo:
        user.Activo = False
        user.save()
    else:
        user.Activo = True
        user.save()
    return HttpResponseRedirect(reverse('Usuarios:user_lists'))
