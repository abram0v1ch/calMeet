from django.db import models
from django.utils.crypto import get_random_string


class Room(models.Model):
    id = models.CharField(primary_key=True, max_length=5, default=(get_random_string(length=5)).upper())


class User(models.Model):
    email = models.EmailField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Calendar(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    url = models.URLField(null=False, default=None)


