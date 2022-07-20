from django.db import models
from datetime import datetime

category_choices = (
	('shoes', 'Shoes'),
	('clothes', 'Clothes'),
	('accessories', 'Accessories')
)

sex_choices = (
	('M', 'Male'),
	('F', 'Female'),
	('U', 'Unisex')
)


class category(models.Model):
	name = models.CharField(max_length=100, blank=False)
	type = models.CharField(
		max_length=100,
		choices=category_choices
	)
	category_of_the_month = models.BooleanField(default=False)
	image = models.ImageField(blank=False, null=False, upload_to='media/%Y/%m/%d/', default='')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "categories"


class product(models.Model):
	category = models.ForeignKey(category, on_delete=models.DO_NOTHING)
	brand = models.CharField(max_length=100, blank=False)
	name = models.CharField(max_length=200, blank=False)
	sex = models.CharField(
		max_length=1,
		choices=sex_choices
	)
	price = models.DecimalField(blank=False, decimal_places=2, max_digits=12)
	description = models.TextField(blank=True, null=True)
	color = models.CharField(max_length=50, blank=False)
	specifications = models.TextField(blank=True, null=True)
	care_info = models.TextField(blank=True, null=True)
	wash_instructions = models.TextField(blank=True, null=True)
	size = models.CharField(max_length=20, blank=False)
	quantity = models.IntegerField(blank=False)
	rating = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)
	comment_num = models.IntegerField(blank=True, null=True)
	featured = models.BooleanField(default=False)
	main_img = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_1 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_2 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=False)
	img_3 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True)
	img_4 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True)
	img_5 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True)
	img_6 = models.ImageField(upload_to='media/%Y/%m/%d/', blank=True, null=True)
	timestamp = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return f"{self.brand} {self.name} in {self.category}"

	class Meta:
		ordering = ['-timestamp']
