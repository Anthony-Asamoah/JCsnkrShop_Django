from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
	path('listings', views.listings, name='shop'),
	path('listing', views.listings, name='listing'),
	path('search', views.listings, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
