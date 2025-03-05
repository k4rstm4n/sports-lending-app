from django.db import models
from django.contrib.auth.models import User
class Equipment(models.Model):
    CONDITION_CHOICES = [
        ('new', 'New'),
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]

    CATEGORY_CHOICES = [
        ('ball', 'Ball Sports'),
        ('racket', 'Racket Sports'),
        ('fitness', 'Fitness Equipment'),
        ('indoor', 'indoor Sports'),
        ('water', 'Water Sports'),
        ('winter', 'Winter Sports'),
        ('extreme', 'extreme Sports')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    brand = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="media/")

    def __str__(self):
        return self.name
