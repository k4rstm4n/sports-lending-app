from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    PRIVACY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
    ]

    collection_name = models.CharField(max_length=100)
    collection_description = models.TextField()
    collection_privacy = models.CharField(max_length=20, choices=PRIVACY_CHOICES)
    collection_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_private_userlist = models.CharField(max_length=100)

    def __str__(self):
        return self.name
