from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    ROLE = (("SA", "SuperAdmin"), ("NA", "NormalAdmin"), ("JA", "Journalist"), ("GU", "GuestUser"))
    role = models.CharField(choices = ROLES,  max_length = 2)
    USERNAME_FIELD = "emial"
    REQUIRED_FIELDS = ("username", "password")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length = 30)
    display_image = models.ImageField(upload_to = "uploads", null = True)

    

