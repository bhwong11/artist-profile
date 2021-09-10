from django.db import models

# Create your models here.
from django.db.models import Model, CharField, PositiveIntegerField, TextField,DateTimeField,URLField,OneToOneField,ManyToManyField,BooleanField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from s3direct.fields import S3DirectField


DEFAULT_USER = 1

class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    is_client = BooleanField(default=False)
    is_in_Chat = BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    MFA_code = PositiveIntegerField(default=0000)

class Tag(Model):
    name = CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name

class Artwork(Model):
    title = CharField(max_length=144, unique=True)
    image = S3DirectField(dest='primary_destination', blank=True)
    description = TextField(max_length=1000)
    date_created = DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='artworks')
    catergory = CharField(max_length=144,default='Misc')
    tags = ManyToManyField(Tag,related_name='artworks')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_created']


class Product(Model):
    name = CharField(max_length=500, unique=True)
    image = S3DirectField(dest='primary_destination', blank=True)
    price = PositiveIntegerField()
    buy_link = URLField()
    catergory = CharField(max_length=300,default='Misc')
    description = TextField(max_length=1000)
    user = ForeignKey(User, on_delete=CASCADE, related_name='products',default=DEFAULT_USER)

    def __str__(self):
        return self.name

class Review(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='reviews')
    user = ForeignKey(User, on_delete=CASCADE, related_name='reviews',default=DEFAULT_USER)
    title = CharField(max_length=300, default='N/A')
    content = TextField(max_length=1000, default='N/A')
    date_created=DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog(Model):
    title = CharField(max_length=300)
    content = TextField(max_length=1000)
    user = ForeignKey(User, on_delete=CASCADE, related_name='blogs')
    date_created=DateTimeField(auto_now_add=True)
