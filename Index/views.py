from django.shortcuts import render

# Create your views here.
def Index(request):
	context = {}
	return render(request, 'Index/dashboard_admin.html', context)