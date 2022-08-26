from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models
from django.urls import reverse


# Create your models here.
class User(BaseUser):
    # custom attributes if desired
    pass