from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('author-list', views.AuthorListAPIView.as_view())

]