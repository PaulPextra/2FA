from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    '''Extending User Model'''
    phone_number = models.CharField(max_length=15)