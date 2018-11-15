from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='users', default='users/default.jpg')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.get_full_name()