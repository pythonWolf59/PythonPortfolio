from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('analyst', 'Analyst'),
        ('viewer', 'Viewer'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    # Add any additional fields you want for your user model

# End of CustomUser model
# Add any additional models you need for your application
