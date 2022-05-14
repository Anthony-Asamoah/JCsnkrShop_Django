from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
	path('search', views.search, name='search'),
	path('listings', views.all_listings, name='shop'),
	path('listings/male', views.male_listings, name='male_shop'),
	path('listings/female', views.female_listings, name='female_shop'),
	path('listing/<int:listing_id>', views.listing, name='listing'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
