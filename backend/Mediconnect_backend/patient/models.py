from django.db import models
from authentication.models import Hospital


# Create your models here.
from accounts.models import User 



class PatientRecord(models.Model):

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name="patients"
    )

    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)

    disease = models.CharField(max_length=200)
    doctor_name = models.CharField(max_length=100)

    admitted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.patient_name