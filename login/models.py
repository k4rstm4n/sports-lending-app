from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
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


class CustomPerms(models.Model):
            
    class Meta:
        
        managed = False  # No database table creation or deletion  \
                         # operations will be performed for this model. 
                
        default_permissions = () # disable "add", "change", "delete"
                                 # and "view" default permissions

        permissions = ( 
            ('borrower_perms', 'Global borrower permissions'),  
            ('lender_perms', 'Global lender permissions'), 
        )