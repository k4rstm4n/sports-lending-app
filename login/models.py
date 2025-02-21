from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddressField(models.Model):
    address = models.CharField(max_length=128)

    city = models.CharField(max_length=64)
    state = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    address = AddressField()

