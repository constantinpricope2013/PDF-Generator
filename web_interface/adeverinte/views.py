from django.shortcuts import render
from .models import Post

# Create your views here.
def adeverinte_home(request):
	context = {
		'posts':Post.objects.all()
	}
	return render(request, 'adeverinte/home.html', context)

def adeverinte_about(request):
	return render(request, 'adeverinte/about.html')