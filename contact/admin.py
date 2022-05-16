from django.contrib import admin
from .models import contact


# Register your models here.


@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
	list_display = ['subject', 'name', 'email', 'complete']
	list_filter = ['complete', 'timestamp']
	search_fields = [i for i in list_display if i != 'complete']
	list_display_links = search_fields
	list_editable = ['complete']
	list_per_page = 20
