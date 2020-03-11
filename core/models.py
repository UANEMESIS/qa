from django.db import models

# Create your models here.
class Car(models.Model):
	vendor = models.CharField(max_length=128)
	model = models.CharField(max_length=128)
	year = models.PositiveSmallIntegerField()
	volume = models.PositiveIntegerField()

	def __str__(self):
		return self.model

class Certificate(models.Model):
	QA = 'QA'
	UAT = 'UAT'
	SERVER_CHOICES = [
		(QA, 'QA'),
		(UAT, 'UAT')
	]
	server = models.CharField(max_length=128, choices=SERVER_CHOICES, default=QA)
	link = models.CharField(max_length=128)
	comment = models.CharField(max_length=256, blank=True)

	def __str__(self):
		return self.link


class Upload(models.Model):
	name = models.TextField(blank=True)
	file = models.ImageField(upload_to='media')
	date = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return str(self.date)

