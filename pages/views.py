from django.shortcuts import render
from .models import text
# Create your views here.


def index(request):
	return render(request, 'pages/index.html')


def about(request):
	info = text.objects.all().values()[0]
	context = {
		'about_body': info['about_body'],
		'services_body': info['services_body'],
		'brands_body': info['brands_body'],
	}
	return render(request, 'pages/about.html', context)
