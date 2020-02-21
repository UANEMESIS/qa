from django.db import models

# Create your models here.
class Car(models.Model):
	vendor = models.CharField(max_length=128)
	model = models.CharField(max_length=128)
	year = models.PositiveSmallIntegerField()
	volume = models.PositiveIntegerField()