from django.db import models

# Create your models here.
class Hospital(models.Model):

    hospital_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default="NA")   # add default
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Patient(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    phone = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)