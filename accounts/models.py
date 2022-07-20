from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class likes(models.Model):
	user = models.ManyToManyField(User)
	liked = models.BooleanField(default=False)
