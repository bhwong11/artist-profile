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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages


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

class ArtworksUpdateView(UpdateView):
    model = Product
    fields = ['name','image','price','buy_link','catergory','description']
    template_name='products/product_update.html'


class ArtworksDeleteView(DeleteView):
    pass


class ProductsView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    #use a form instance and a for loop to pass to pass in context[form{review.id}]

class ProductShowView(DetailView):
    model=Product
    template_name = 'products/product_show.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user_create_from'] = UserCreationForm()
        return context

class ProductsCreateView(CreateView):
    model=Product
    fields=['name','image','price','buy_link','catergory','description']
    template_name = 'product_new.html'
    success_url = '/products/'

class UpdateProductView(UpdateView):
    model = Product
    fields = ['name','image','price','buy_link','catergory','description']
    template_name='products/product_update.html'

    def get_success_url(self):
        return reverse("product_show",kwargs={'pk':self.object.pk})


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'product_delete_confirmation.html'
    success_url = '/products/'

class ReviewsCreateView(View):
    def post(self,request):
        if request.user:
            title = request.POST.get('title')
            content = request.POST.get('content')
            user = request.user
            product = Product.objects.get(pk=request.POST.get('product'))
            new_review = Review.objects.create(title=title,content=content,user=user,product=product)
            return redirect(f'/products/{new_review.product.pk}')
        else:
            product = request.POST.get('product')
            return redirect(f'/products/{product}')


class ReviewsUpdateView(View):
    def post(self,request,pk):
        title = request.POST.get('title')
        content = request.POST.get('content')
        review = Review.objects.get(pk=pk)
        updated_review = Review.objects.filter(pk=pk).update(title=title,content=content)
        return redirect(f'/products/{review.product.pk}')

class ReviewsDeleteView(View):
    def post(self,request,pk):
        review = Review.objects.get(pk=pk)
        Review.objects.filter(pk=pk).delete()
        return redirect(f'/products/{review.product.pk}')

class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        product_pk = request.POST.get('product')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/products/{product_pk}')

        else:
            messages.add_message(request, messages.WARNING, 'The Username or Password was Inccorect')
            return redirect(f'/products/{product_pk}')

class LogoutView(View):
    def post(self,request):
        product_pk = request.POST.get('product')
        logout(request)
        return redirect(f'/products/{product_pk}')

class SignupView(View):
    def post(self,request):
        product_pk = request.POST.get('product')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            Profile.objects.create(user=request.user,isClient=False)
            return redirect(f'/products/{product_pk}')
        else:
            messages.add_message(request, messages.WARNING, form.errors)
            return redirect(f'/products/{product_pk}')