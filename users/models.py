from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email=models.EmailField(unique=True)




class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, blank=True , default="")
    phone_number = models.CharField(max_length=25, blank=True, default="")
    bio = models.TextField( blank=True, default="")
    profile_picture = models.ImageField(
        upload_to='profile_picture/%Y/%m/%d', blank=True
    )

    def __str__(self):
        return f"Profile of {self.seller.username}"