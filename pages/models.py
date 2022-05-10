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


class brand(models.Model):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-timestamp']
