from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.
class User(AbstractUser):
    pass

admin.site.register(User)