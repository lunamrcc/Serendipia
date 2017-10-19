from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Usuarios

from .forms import UsuariosForm


# Create your views here.

# def login(request):
#     email = request.POST.get('Email', False)
#     password = request.POST.get('Password', False)
#     user = Usuarios.objects.filter(Email=email)
#     if user.count() > 0:
#         user = Usuarios.objects.filter(Email=email, Passwd=password)
#         if user.count() > 0:
#             context ={}
#             return render(request, 'Index/login.html',context)
#         else:
#             return HttpResponseRedirect(reversed('Index/login.html'))
#     else:
#         return HttpResponseRedirect(reversed('Index/login.html'))

def user_lists(request):
    all_users = Usuarios.objects.all()
    context ={
        'all_users': all_users
        }
    return render(request, 'Usuarios/usuarios_list.html',context)

def user_create(request):
    context = {}
    NewUsuariosForm = UsuariosForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        NewUsuariosForm = UsuariosForm(request.POST)
        UserValid = NewUsuariosForm.is_valid()

        # check whether it's valid
        if UserValid:
            Usu = NewUsuariosForm.save(commit=False)
            Usu.Activo = True
            ID = Usuarios.objects.count() + 1
            Usu.Usuarioid = ID
            Usu.save()
            return user_lists(request)

    context = {
        'NewUsuariosFrom': NewUsuariosForm
    }
    return render(request, 'Usuarios/usuarios_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'Usuarios/usuarios_form.html', context)




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
