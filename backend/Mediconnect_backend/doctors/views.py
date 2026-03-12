from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializer import DoctorSerializer
# Create your views here.
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer