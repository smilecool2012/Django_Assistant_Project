from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='email_confirmed', on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
