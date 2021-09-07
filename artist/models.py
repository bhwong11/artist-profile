from django.db import models

# Create your models here.
from django.db.models import Model, CharField, PositiveIntegerField, TextField,DateTimeField
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE
from s3direct.fields import S3DirectField

class Artwork(Model):
    title = CharField(max_length=144, unique=True)
    image = S3DirectField(dest='primary_destination', blank=True)
    description = TextField(max_length=1000)
    published_date = DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='artworks')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published_date']

class Products(Model):
    name = CharField(max_length=500, unique=True)
    image = S3DirectField
    price = PositiveIntegerField