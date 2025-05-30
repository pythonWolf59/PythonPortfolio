from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .serializers import UserCreateSerializer
from .models import CustomUser

class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users (admin) can create
