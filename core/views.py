from django.shortcuts import render
from django.http import JsonResponse
from .models import Car, Certificate, Upload
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt







#from django.shortcuts import render
#from django.views.decorators.csrf import csrf_exempt
#from .models import Product, Upload
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CertificateSerializer, UploadSerializer
from django.core import serializers
from rest_framework import status
#from django.db.models import F
from django.db.models import Q
#import json
from rest_framework.pagination import (LimitOffsetPagination, PageNumberPagination,)



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


def all_certificates(request):
	result = []
	certs = Certificate.objects.all()
	for crt in certs:
		#print(usr)
		result.append({
			"server": str(crt.server),
			"link": str(crt.link),
			"comment": str(crt.comment)

			})

	return JsonResponse(result, safe=False)

@csrf_exempt
def upload_image(request):
	msg = {"status": "Good"}
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		#print(request.data)
		#print(request.FILES)
		return JsonResponse({"test"}, safe=False, status=200)
	elif request.method == 'GET':
		pass
	else:
		message = {"error": "Unsupported method!"}
		return JsonResponse(message, safe=False, status=405)


# API SECTION
@csrf_exempt
@api_view(['GET', 'POST',])
@permission_classes([AllowAny, ])  #AllowAny #IsAuthenticated
def upload_image(request):
	item = request.data
	if request.method == 'POST':
		serializer = UploadSerializer(data=item)
		serializer.is_valid(raise_exception=True) # returns 400 Bad request > ok!
		serializer.save()
		return Response({"message": "Upload created!"}, status=status.HTTP_201_CREATED) #, "data": request.data}
	else:
		all_obj = Upload.objects.filter().order_by('id')
		#if len(all_obj) > 0:
			#pagination - good solution 
			#https://stackoverflow.com/questions/29128225/django-rest-framework-3-1-breaks-pagination-paginationserializer
			#paginator = PageNumberPagination()
			
			#paginator = PageNumberPagination()
			#result_page = paginator.paginate_queryset(all_obj, request)
			#serializer = ProductSerializer(result_page, many=True)
			#return Response(serializer.data, status=status.HTTP_200_OK)
		paginator = PageNumberPagination()
		result_page = paginator.paginate_queryset(all_obj, request)
		#if result_page is not None:
		serializer = UploadSerializer(result_page, many=True)
		return paginator.get_paginated_response(serializer.data)
		#a = paginator.get_paginated_response(serializer.data)
		#else:
		#return Response(a, status=status.HTTP_200_OK)
			#return Response({"message": "There is no created items!"}, status=status.HTTP_200_OK)
