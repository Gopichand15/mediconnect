from django.urls import path
from .views import DoctorListCreateView,DoctorDetailView

urlpatterns= [
    path('',DoctorListCreateView.as_view()),#GET,POST
    path('<int:pk>/',DoctorDetailView.as_view()),#PUT,DELETE
]
