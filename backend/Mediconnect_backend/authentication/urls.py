from django.urls import path
from .views import *

urlpatterns = [

    path('hospital/register/', HospitalRegisterView.as_view()),
    path('hospital/login/', HospitalLoginView.as_view()),

    path('patient/register/', PatientRegisterView.as_view()),
    path('patient/login/', PatientLoginView.as_view()),
]