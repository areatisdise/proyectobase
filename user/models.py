from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    DniUsu = models.CharField(max_length=8, unique=True, blank=False)

