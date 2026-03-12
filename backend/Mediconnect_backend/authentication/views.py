
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital, Patient
from .serializers import HospitalSerializer, PatientSerializer
import random


# -------------------------------
# Hospital Registration
# -------------------------------

class HospitalRegisterView(generics.CreateAPIView):

    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Hospital registered successfully"
            })

        return Response(serializer.errors)


# -------------------------------
# Hospital Login
# -------------------------------

class HospitalLoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        try:

            hospital = Hospital.objects.get(
                username=username,
                password=password
            )

            return Response({
                "status": True,
                "message": "Login successful",
                "hospital_name": hospital.hospital_name
            })

        except Hospital.DoesNotExist:

            return Response({
                "status": False,
                "message": "Invalid username or password"
            })


# -------------------------------
# Patient Registration (OTP)
# -------------------------------

class PatientRegisterView(APIView):

    def post(self, request):

        name = request.data.get("name")
        age = request.data.get("age")
        phone = request.data.get("phone")

        otp = random.randint(1000, 9999)

        patient = Patient.objects.create(
            name=name,
            age=age,
            phone=phone,
            otp=otp
        )

        return Response({
            "status": True,
            "message": "OTP sent successfully",
            "otp": otp
        })


# -------------------------------
# Patient Login With OTP
# -------------------------------

class PatientLoginView(APIView):

    def post(self, request):

        phone = request.data.get("phone")
        otp = request.data.get("otp")

        try:

            patient = Patient.objects.get(
                phone=phone,
                otp=otp
            )

            return Response({
                "status": True,
                "message": "Login successful",
                "patient_name": patient.name
            })

        except Patient.DoesNotExist:

            return Response({
                "status": False,
                "message": "Invalid OTP"
            })