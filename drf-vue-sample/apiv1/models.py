from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    REQUIRED_FIELDS = ['email', 'is_staff', 'is_active', 'is_superuser']
