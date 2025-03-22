from django.db import models
from django.contrib.auth.models import User
from login.models import CustomPerms


class Collection(models.Model):

    collection_name = models.CharField(max_length=100)
    collection_description = models.TextField()
    # if User.get_user_permissions("login.lender_perms"):
    PRIVACY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
    ]
    collection_privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES)
    # else:
    #     collection_privacy = ("public", "Public")
    collection_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_private_userlist = models.CharField(max_length=100)

    def __str__(self):
        return self.name
