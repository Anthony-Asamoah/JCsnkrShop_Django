from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from .models import contact as form


# Create your views here.


def contact(request):
	if request.method == 'POST':
		temp = form(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message']
		)
		with transaction.atomic():
			temp.save()
		messages.success(request, ' - Message Received. An agent shall reply shortly')

	return render(request, 'contact/Contact.html')
