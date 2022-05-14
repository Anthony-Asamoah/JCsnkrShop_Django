from django.db import models
from datetime import datetime


# Create your models here.


class contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	message = models.TextField(null=False, blank=False)
	timestamp = models.DateTimeField(default=datetime.now())
	complete = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.subject} from {self.name}"

	class Meta:
		ordering = ['-timestamp']
