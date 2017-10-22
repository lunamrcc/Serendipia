from .models import SSInstituciones
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import UpdateView

from .forms import InstForm


# Create your views here.
def inst_lists(request):
    all_inst = SSInstituciones.objects.all()
    context ={
        'all_inst': all_inst
        }
    return render(request, 'SSInstituciones/instituciones_list.html',context)

def inst_delete(request, pk):
    inst = SSInstituciones.objects.filter(institucionID=pk)
    inst.delete()
    return HttpResponseRedirect(reverse('SSInstituciones:inst_lists'))


def inst_create(request):
    context = {}
    NewInstForm = InstForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request
        NewInstForm = InstForm(request.POST)
        InstValid = NewInstForm.is_valid()

        # check whether it's valid
        if InstValid:
            Inst = NewInstForm.save(commit=False)
            Inst.Activo = True
            ID = Instituciones.objects.count() + 1
            Inst.institucionID = ID
            Inst.save()
            return inst_lists(request)

    context = {
        'NewInstForm': NewInstForm
    }
    return render(request, 'SSInstituciones/instituciones_form.html', context)

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'SSInstituciones/instituciones_form.html', context)



class inst_update(UpdateView):
    model = SSInstituciones
    fields = [
        'nombre',
        'direccion',
        'telefono',
        'coordenadaX',
        'coordenadaY'
    ]
    template_name = 'SSInstituciones/instituciones_edit_form.html'

    success_url = reverse_lazy('SSInstituciones:inst_lists')
