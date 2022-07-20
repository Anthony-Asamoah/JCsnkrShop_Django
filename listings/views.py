import logging

from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.core.paginator import Paginator


class common:
	products = models.product.objects.all()
	categories = models.category.objects.all()

	category_type = []
	for i in categories:
		category_type.append(i.type)
	category_type = set(category_type)


def sieve(item):
	# get queryset
	products = common.products
	logging.info(products)

	# get filter
	logging.info(item)
	if item in models.category_choices:
		products.filter(category=item)
	if item in models.sex_choices:
		products.filter()

	# select filter
	# apply filter
	# return queryset
	pass


# ################################################################# #

def all_listings(request, item=None):
	products = sieve(item)
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
	if product.specifications:
		prod_spec = product.specifications.split("\n")
	else:
		prod_spec = product.specifications

	related = common.products.filter(
		sex=product.sex,
		# category=product.category,
	).exclude(id=product.id)[:5]

	try:
		related[:12]
	except Exception:
		pass

	context = {
		'listing': product,
		'specifications': prod_spec,
		'description': prod_description,
		'related': related
	}
	return render(request, 'listings/listing.html', context)


def search(request):
	keywords = request.GET['search']
	if keywords:
		context = {
			'listings': common.products.filter(name__icontains=keywords)
		}
		return render(request, 'listings/listings.html', context)

	return redirect('shop')
