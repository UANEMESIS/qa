from django.shortcuts import render
from django.http import JsonResponse
from .models import Car
from django.contrib.auth.models import User

# Create your views here.
def all_cars(request):
	result = []
	cars = Car.objects.all()
	for car in cars:
		result.append({
			"vendor": car.vendor,
			"model": car.model,
			"year": car.year,
			"volume": car.volume
			})


	return JsonResponse(result, safe=False)

def all_users(request):
	result = []
	users = User.objects.all()
	for usr in users:
		#print(usr)
		result.append({
			"username": str(usr)
			})

	return JsonResponse(result, safe=False)
