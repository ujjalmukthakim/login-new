from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.

# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     email=models.EmailField(unique=True)
#     username=models.TextField(max_length=100)
#     is_active=models.BooleanField(default=False)
#     is_varified=models.BooleanField(default=False)
