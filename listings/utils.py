from django.core.paginator import Paginator
from . import models
from pages.models import text

import logging


class common:
	products = models.product.objects.all()
	categories = models.category.objects.all()

	category_type = []
	for i in categories:
		category_type.append(i.type)
	category_type = set(category_type)


def sieve(category=False, sex='U'):
	products = common.products

	if sex != 'U':
		logging.debug(f'sex: {sex}')
		products = products.filter(sex=sex)

	elif category:
		logging.debug(f"category: {category}")
		products = products.filter(category__name=category)

	return products


def brands_text():
	info = text.objects.all().values()[0]
	return info['brands_body']


def single_page(products, request):
	paginator = Paginator(products, 9)
	return paginator.get_page(request.GET.get('page'))
