from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.core.paginator import Paginator


def sieve(self, sex, query):
	final = query.filter(sex=sex)
	return final


class common:
	products = models.product.objects.all()
	categories = models.category.objects.all()

	category_type = []
	for i in categories:
		category_type.append(i.type)
	category_type = set(category_type)


# ################################################################# #

def all_listings(request):
	paginator = Paginator(common.products, 9)
	single_page = paginator.get_page(request.GET.get('page'))

	context = {
		'listings': single_page,
		'category_type': common.category_type,
		'categories': common.categories
	}
	return render(request, 'listings/listings.html', context)


def male_listings(request):
	products = common.products.filter(sex='M')

	paginator = Paginator(products, 9)
	single_page = paginator.get_page(request.GET.get('page'))

	context = {
		'listings': single_page,
		'category_type': common.category_type,
		'categories': common.categories
	}
	return render(request, 'listings/listings.html', context)


def female_listings(request):
	products = common.products.filter(sex='F')

	paginator = Paginator(products, 9)
	single_page = paginator.get_page(request.GET.get('page'))
	context = {
		'listings': single_page,
		'category_type': common.category_type,
		'categories': common.categories
	}
	return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
	product = get_object_or_404(models.product, pk=listing_id)
	prod_description = product.description.split("\n")
	prod_spec = product.specifications.split("\n")

	context = {
		'listing': product,
		'specifications': prod_spec,
		'description': prod_description
	}
	return render(request, 'listings/listing.html', context)


def search(request):
	if request.method == 'POST':

		context = {common.products.filter()}
		return render(request, 'listings/listings.html', context)

	return redirect('shop')
