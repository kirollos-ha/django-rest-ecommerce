from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    # email = models.EmailField(_('email address'), blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.EmailField("email address", blank=False, unique=True)
