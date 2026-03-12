from django.urls import path
from .views import *

urlpatterns = [

    path('add/', AddPatientView.as_view()),
    path('list/', PatientListView.as_view()),
    path('update/<int:id>/', PatientUpdateView.as_view()),
    path('delete/<int:id>/', PatientDeleteView.as_view()),

]