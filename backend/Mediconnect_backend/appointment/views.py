from rest_framework import generics
from .models import Appointment
from .serializer import AppointmentSerializer


class AppointmentListView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer