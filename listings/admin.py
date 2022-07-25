from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.category)
class categoryAdmin(admin.ModelAdmin):
	list_display = ['type', 'name', 'category_of_the_month']
	list_editable = ['category_of_the_month']
	search_fields = ['name']
	list_filter = [i for i in list_display if i != 'name']
	list_per_page = 20


@admin.register(models.product)
class productAdmin(admin.ModelAdmin):
	list_display = [
		'category', 'brand', 'sex', 'color', 'name',
		'size', 'quantity', 'price', 'featured'
	]

	list_editable = [
		'featured'
	]

	list_filter = [
		'featured', 'category', 'brand', 'sex',
		'color', 'size', 'timestamp'
	]
	list_display_links = [i for i in list_display if i != 'featured']
	search_fields = list_display
	list_per_page = 50
