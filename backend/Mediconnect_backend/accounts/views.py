from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializer import UserSerializer


# Register / list users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Retrieve / update / delete user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer