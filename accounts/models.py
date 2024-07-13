from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  # Additional field for user's age
    is_admin = models.BooleanField(default=False)  # Flag to indicate if user is an admin

    def __str__(self):
        return self.username
