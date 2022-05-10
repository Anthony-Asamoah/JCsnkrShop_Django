from django.shortcuts import render

# Create your views here.


def listings(request):

	context = {

	}
	return render(request, 'listings/listings.html', context)


def listing(request):
	if request.method == 'POST':

		context = {

		}
		return render(request, 'listings/listing.html', context)

	else:

		context = {

		}
		return render(request, 'listings/listing.html', context)
