from django.db import models

# Create your models here.
class AddressField(models.Model):
    address = models.CharField(max_length=128)

    city = models.CharField(max_length=64)
    state = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=5)
class Profile(models.Model):
    username = models.CharField(max_length=32)
    passward = models.CharField(max_length=32)
    birth_date = models.DateField()
    address = AddressField()

