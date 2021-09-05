from django.shortcuts import render, redirect

from django.views import View
from django.views.generic.base import TemplateView

from .models import Artwork

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

