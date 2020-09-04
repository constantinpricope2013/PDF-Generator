from django.shortcuts import render

# Create your views here.
def adeverinte_home(request):
	context = {
	}
	return render(request, 'adeverinte/home.html', context)