from django.urls import path
from .views import *

urlpatterns = [

path('hospital/register/',hospital_register),
path('hospital/login/',hospital_login),

path('patient/register/',patient_register),
path('patient/login/',patient_login),

]