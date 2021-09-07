from django import forms
from s3direct.widgets import S3DirectWidget

class S3DirectUploadForm(forms.Form):
    title = forms.CharField(max_length=1000, required=False, widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    image = forms.Field(widget=S3DirectWidget(dest='primary_destination', attrs={'class': 'file-input'}),required=False)
    description = forms.CharField(widget=forms.Textarea)