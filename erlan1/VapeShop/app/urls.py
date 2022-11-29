

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexList.as_view())
]