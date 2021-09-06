from django.shortcuts import render, redirect

from django.views import View
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
        redirect('home.html')

    def get_success_url(self):
        return reverse("home")

class ArtworksView(TemplateView):
    template_name = 'artwork_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artworks'] = Artwork.objects.all()
        return context
