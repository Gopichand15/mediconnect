from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Hospital  
from .serializer import HospitalSerializer

# Create your views here.
class HospitalView(generics.ListCreateAPIView):
    queryset=Hospital.objects.all()
    serializer_class=HospitalSerializer