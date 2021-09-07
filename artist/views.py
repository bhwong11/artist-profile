from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse

from .models import Artwork
from django.views.generic import FormView
from .forms import S3DirectUploadForm


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class ArtworkView(FormView):
    template_name = 'create_test.html'
    form_class = S3DirectUploadForm

    def post(self,request):
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')
        Artwork.objects.create(title = title,image =image,description=description)
        return redirect('home')

class ArtworksView(FormView):
    template_name = 'artwork_index.html'
    form_class = S3DirectUploadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = S3DirectUploadForm(initial={'title': 'foo'})
        image=Artwork.objects.get(title='h')
        print(image.image)
        context['form'] = S3DirectUploadForm(initial={'title': 'foo','image':image.image})
        context['artworks'] = Artwork.objects.all()
        return context
