from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # The class user takes inheritance from AbstractUser to let django create
    # meaningfull users in its system.

    # Abstract users comes with certain defaults, the required ones are username and
    # password.

    # Some other fields that are included but optional are first_name, last_name and 
    # email.

    # Extra fields to the user model

    profile_picture = models.ImageField()
    followers = models.IntegerField(blank=True, default=0)
    posts = models.IntegerField(blank=True, default=0)
    likes = models.IntegerField(blank=True, default=0)

