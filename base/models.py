from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

#tell django to replace the field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []