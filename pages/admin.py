from django.contrib import admin
from .models import text


# Register your models here.


@admin.register(text)
class textAdmin(admin.ModelAdmin):
	list_display = ['about_body', 'services_body', 'brands_body']
