from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.



class Vehicle(models.Model):
    vehicle_number=models.PositiveIntegerField()
    model=models.CharField(max_length=200)
    options=(("Two","Two"),("Three","Three"),("Four","Four"))
    vehicle_type=models.CharField(max_length=200,choices=options)
    vehicle_description=models.CharField(max_length=200)

    def __str__(self):
        return self.vehicle_number

class User(AbstractUser):
    ROLE_CHOICES=(
        ('superadmin','Super Admin'),
        ('admin','Admin'),
        ('user','User')
    )
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)