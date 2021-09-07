from django import forms
from django.db.models.query import QuerySet
from s3direct.widgets import S3DirectWidget
from .models import Artwork,Profile,Tag,Product,Review,Blog,User

class ArtworkForm(forms.Form):
    title = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    image = forms.Field(widget=S3DirectWidget(dest='primary_destination', attrs={'class': 'file-input'}),required=False)
    description = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    catergory = forms.CharField(max_length=144,required=False,)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())