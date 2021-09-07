from django.contrib import admin
from .models import Artwork,Profile,Tag,Product,Review,Blog

# Register your models here.
admin.site.register(Artwork)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Blog)
