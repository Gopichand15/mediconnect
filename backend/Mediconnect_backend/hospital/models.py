from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)

    