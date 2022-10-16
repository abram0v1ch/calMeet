from django.db import models
from django.utils.crypto import get_random_string


def generate_id_length():
    return get_random_string(length=5)


class Room(models.Model):
    id = models.CharField(primary_key=True, max_length=5, default=generate_id_length().upper())


class User(models.Model):
    email = models.EmailField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Calendar(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    url = models.URLField(null=False, default=None)


