from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse

from .models import Artwork
from django.views.generic import FormView
from .forms import ArtworkForm


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class ArtworkView(FormView):
    template_name = 'create_test.html'
    form_class = ArtworkForm

    def post(self,request):
        title = request.POST.get('title')
        image = request.POST.get('image')
        description = request.POST.get('description')
        Artwork.objects.create(title = title,image =image,description=description)
        return redirect('artworks')

class ArtworksView(TemplateView):
    template_name = 'artwork_index.html'
    form_class = ArtworkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ArtworkForm(initial={'title': 'foo'})
        image=Artwork.objects.get(title='h')
        print(image.image)
        context['form'] = ArtworkForm(initial={'title': 'foo','image':image.image})
        context['artworks'] = Artwork.objects.all()
        return context

class ProductsView(TemplateView):
    pass

class UpdateProductView(TemplateView):
    pass

class ProductShowView(TemplateView):
    pass

class DeleteProductView(View):
    pass