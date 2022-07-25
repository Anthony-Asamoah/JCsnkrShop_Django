from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .utils import common, sieve, single_page, brands_text
from pages.views import brands


context = {
	'category_type': common.category_type,
	'categories': common.categories,
	'brands': brands(),
	'brands_body': brands_text()
}


def all_listings(request, item=False):
	context.update({'listings': single_page(sieve(category=item), request)})
	return render(request, 'listings/listings.html', context)


def male_listings(request):
	context.update({'listings': single_page(sieve(sex='M'), request)})
	return render(request, 'listings/listings.html', context)


def female_listings(request):
	context.update({'listings': single_page(sieve(sex='F'), request)})
	return render(request, 'listings/listings.html', context)


def search(request):
	keywords = request.GET['search']
	if keywords:
		context = {
			'listings': common.products.filter(name__icontains=keywords)
		}
		return render(request, 'listings/listings.html', context)

	return redirect('shop')


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
	).exclude(id=product.id)

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
