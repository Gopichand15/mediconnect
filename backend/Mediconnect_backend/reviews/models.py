from django.db import models
from patient.models import Patient
from doctors.models import Doctor

class Review(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
