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
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class Review(models.Model):
#     equipment = models.ForeignKey(
#         Equipment, on_delete=models.CASCADE, related_name="reviews"
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     rating = models.PositiveSmallIntegerField(
#         choices=[(i, str(i)) for i in range(1, 6)]
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
