from django import forms
from s3direct.widgets import S3DirectWidget

class S3DirectUploadForm(forms.Form):
    title = forms.CharField(max_length=1000, required=False)
    image = forms.Field(widget=S3DirectWidget(dest='primary_destination'),required=False)
    description = forms.CharField(widget=forms.Textarea)