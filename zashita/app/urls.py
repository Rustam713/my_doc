from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, about, contact, glasses, shop, register, mylogin, mylogout


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('glasses/', glasses, name='glasses'),
    path('shop/', shop, name='shop'),
    path('register/', register, name='register'),
    path('login/', mylogin, name='login'),
    path('logout', mylogout, name='logout'),
]