from django.db import models

# Create your models here.
class Hospital(models.Model):
   
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    

    