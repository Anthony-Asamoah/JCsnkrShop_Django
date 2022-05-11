from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.category)
class categoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'category_of_the_month',]
	list_editable = ['category_of_the_month']
	search_fields = ['name']
	list_filter = list_display
	list_per_page = 10




@admin.register(models.product)
class productAdmin(admin.ModelAdmin):
	list_display = [
		'category', 'brand', 'color', 'name',
		'size', 'quantity', 'price', 'featured'
	]

	list_editable = [
		'featured'
	]

	list_display_links = [i for i in list_display if i != 'featured']
	search_fields = list_display
	list_filter = list_display
	list_per_page = 50
