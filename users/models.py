from django.db import models
from django.contrib.auth.models import AbstractUser #FOR CUSTOM USER MODEL

class CustomUser(AbstractUser):
    # Extra customs columns should go here..
    age = models.PositiveIntegerField(null=True,blank=True) # a new custom field




