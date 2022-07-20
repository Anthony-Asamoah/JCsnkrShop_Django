from django.shortcuts import render
from .models import text
from listings.models import product, category

# Create your views here.


def index(request):
	context = {
		'products': product.objects.filter(featured=True)[:3],
		'categories': category.objects.filter(category_of_the_month=True)[:3],
		'recommended': product.objects.filter()
	}

	return render(request, 'pages/index.html', context)


def about(request):
	info = text.objects.all().values()[0]
	context = {
		'about_body': info['about_body'],
		'services_body': info['services_body'],
		'brands_body': info['brands_body'],
	}
	return render(request, 'pages/about.html', context)
