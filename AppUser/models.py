from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='user_profile_images', null=True, blank=True)

    def __str__(self):
        return self.username

class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name