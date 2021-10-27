from django.db import models
from django.db.models import aggregates

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField()
