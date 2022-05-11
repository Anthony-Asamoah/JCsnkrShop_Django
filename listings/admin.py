from django.contrib import admin
from .models import product

# Register your models here.


@admin.register(product)
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
