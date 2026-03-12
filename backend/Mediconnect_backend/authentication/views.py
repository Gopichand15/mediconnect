from django.shortcuts import render

# Create your views here.

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hospital,Patient
from .serializers import HospitalSerializer, PatientSerializer
import random


# -------------------------------
# Hospital Registration
# -------------------------------

@api_view(['POST'])
def hospital_register(request):

    serializer = HospitalSerializer(data=request.data)
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

@api_view(['POST'])
def hospital_login(request):

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

@api_view(['POST'])
def patient_register(request):

    name = request.data.get("name")
    age = request.data.get("age")
    phone = request.data.get("phone")

    otp = random.randint(1000,9999)

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

@api_view(['POST'])
def patient_login(request):

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