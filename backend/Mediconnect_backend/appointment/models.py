from django.db import models
from django.db import models
from patient.models import PatientRecord
from doctors.models import Doctor
# Create your models here.


class Appointment(models.Model):

    STATUS = (
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('completed','Completed'),
        ('cancelled','Cancelled'),
    )

    patient = models.ForeignKey(PatientRecord,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10,choices=STATUS)