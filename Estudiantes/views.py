from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Estudiantes

from .forms import EstudiantesForm


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

def student_lists(request):
    all_students = Estudiantes.objects.all()
    context ={
        'all_students': all_students
        }
    return render(request, 'Estudiantes/student_list.html',context)

def student_create(request):
    context = {}
    NewEstudiantesForm = EstudiantesForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        NewEstudiantesForm = EstudiantesForm(request.POST)
        StudentValid = NewEstudiantesForm.is_valid()

        # check whether it's valid
        if StudentValid:
            Est = NewEstudiantesForm.save(commit=False)
            Est.Activo = True
            ID = Estudiantes.objects.count() + 1
            Est.EstudianteID = ID
            Est.save()
            return student_lists(request)

    context = {
        'NewEstudiantesForm': NewEstudiantesForm
    }
    return render(request, 'Estudiantes/student_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'Estudiantes/student_form.html', context)




def student_delete(request, pk):
    student = Estudiantes.objects.filter(EstudianteID=pk)
    student.delete()
    return HttpResponseRedirect(reverse('Estudiantes:student_lists'))

def student_change_status(request, pk):
    student = Estudiantes.objects.get(EstudianteID=pk)
    if student.Activo:
        student.Activo = False
        student.save()
    else:
        student.Activo = True
        student.save()
    return HttpResponseRedirect(reverse('Estudiantes:student_lists'))