"""qa_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import all_cars, all_users, all_certificates, upload_image
# from .views import home_page
# from django.views.generic import TemplateView

urlpatterns = [
    path('cars/', all_cars),
    path('users/', all_users),
    path('certificates/', all_certificates),
    path('upload/', upload_image)
    #path('', home_page),
    # path("", TemplateView.as_view(template_name="home.html"),name="app",),
]
