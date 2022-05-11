from django.db import models
from datetime import datetime

# Create your models here.


class text(models.Model):
	about_body = models.TextField()
	services_body = models.TextField()
	brands_body = models.TextField()

	def __str__(self):
		return "Text info"

	class Meta:
		ordering = ['pk']
