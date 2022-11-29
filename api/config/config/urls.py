"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from app.views import *
from .urls_yasg import urlpatterns_yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/car/crete/', CarCreateView.as_view()),
    path('api/v1/car/list/', CarListView.as_view()),
    path('api/v1/car/detail/<int:pk>', CarDetailView.as_view()),
] + urlpatterns_yasg
