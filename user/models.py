from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

class AuthUser(models.Model):
    auth_user_id = models.BigIntegerField()
