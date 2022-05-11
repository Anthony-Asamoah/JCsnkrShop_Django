from django.db import models

# Create your models here.


class category(models.Model):
	name = models.CharField(max_length=100, blank=False)
	category_of_the_month = models.BooleanField(default=False)


class product(models.Model):
	category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
	brand = models.CharField(max_length=100, blank=False)
	name = models.CharField(max_length=200, blank=False)
	price = models.IntegerField(blank=False)
	description = models.TextField()
	color = models.CharField(max_length=50, blank=False)
	specifications = models.TextField()
	size = models.CharField(max_length=20, blank=False)
	quantity = models.IntegerField(blank=False)
	rating = models.IntegerField()
	comment_num = models.IntegerField()
	featured = models.BooleanField(default=False)
	main_img = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_1 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_2 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_3 = models.ImageField(upload_to='media/%Y/%m/%d/')
	img_4 = models.ImageField(upload_to='media/%Y/%m/%d/')
	img_5 = models.ImageField(upload_to='media/%Y/%m/%d/')
	img_6 = models.ImageField(upload_to='media/%Y/%m/%d/')

	def __str__(self):
		return f"{self.brand} {self.name} in {self.category}"
