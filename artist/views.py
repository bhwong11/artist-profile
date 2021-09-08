from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse

from .models import Artwork, Product,Tag,Review,Profile,Blog
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
    template_name = 'artwork_list.html'
    form_class = ArtworkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image=Artwork.objects.get(title='h')
        print(image.image)
        context['form'] = ArtworkForm(initial={'title': 'foo','image':image.image})
        context['artworks'] = Artwork.objects.all()
        return context

class ProductsView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductShowView(DetailView):
    model=Product
    template_name = 'product_show.html'

class ProductsCreateView(CreateView):
    model=Product
    fields=['name','image','price','buy_link','catergory','description']
    template_name = 'product_new.html'
    success_url = '/products/'

class UpdateProductView(UpdateView):
    model = Product
    fields = ['name','image','price','buy_link','catergory','description']
    template_name='product_update.html'

    def get_success_url(self):
        return reverse("product_show",kwargs={'pk':self.object.pk})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product_delete_confirmation.html'
    success_url = '/products/'
