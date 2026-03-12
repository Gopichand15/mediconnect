from rest_framework import generics
from .models import PatientRecord
from .serializers import PatientRecordSerializer


# Add Patient
class AddPatientView(generics.CreateAPIView):

    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer


# View All Patients
class PatientListView(generics.ListAPIView):

    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer


# Update Patient
class PatientUpdateView(generics.UpdateAPIView):

    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    lookup_field = "id"


# Delete Patient
class PatientDeleteView(generics.DestroyAPIView):

    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    lookup_field = "id"