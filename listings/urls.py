from django.urls import path
from . import views


urlpatterns = [
	path('listings', views.listings, name='shop'),
	path('listing', views.listings, name='listing'),
	path('search', views.listings, name='search'),
]