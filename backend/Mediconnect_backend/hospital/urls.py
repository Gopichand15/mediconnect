from django.urls import path
from .views import HospitalView


urlpatterns=[
    path('create/',HospitalView.as_view()),
]