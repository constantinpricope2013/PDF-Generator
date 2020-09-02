from django.shortcuts import render

posts = [
	{
		'title':"Title",
		'data_publish': "20 Feb 2020",
		'time_publish': "20:12",
		'content':"Prima noutate postat pe aplicatie"
	},
	{
		'title':"Second Title",
		'data_publish': "22 Feb 2020",
		'time_publish': "10:12",
		'content':"A doua noutate postat pe aplicatie"
	}
]

# Create your views here.
def adeverinte_home(request):
	context = {
		'posts':posts
	}
	return render(request, 'adeverinte/home.html', context)

def adeverinte_about(request):
	context = {
		'posts':posts
	}
	return render(request, 'adeverinte/about.html', context)