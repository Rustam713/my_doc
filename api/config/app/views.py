
from rest_framework import generics
from .serializers import *
from .models import Car
from .permissions import IfIsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAdminUser, ]

class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, ]

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = [IfIsOwner, IsAuthenticated]
