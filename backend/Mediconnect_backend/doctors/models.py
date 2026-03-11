from django.db import models
from hospital.models import Hospital
# Create your models here.

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()

    doctor_image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='doctors'
    )