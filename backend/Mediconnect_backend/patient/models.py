from django.db import models

# Create your models here.
from accounts.models import User 

# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
