from django.shortcuts import render, redirect

from django.views import View
from django.http import HttpResponse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.urls import reverse

from .models import Artwork, Product,Tag,Review,Profile,Blog,User
from django.views.generic import FormView
from .forms import ArtworkForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework import generics
from twilio.rest import Client
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from random import randint
import threading


# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')

class ArtworkCreateView(CreateView):
    model = Artwork
    template_name = 'artwork/artwork_create.html'
    fields = ['title','image','description','catergory','tags']
    success_url = '/artworks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(ArtworkCreateView, self).form_valid(form)
        return redirect('/artworks/')

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')

class ArtworksView(TemplateView):
    template_name = 'artwork/artwork_list.html'
    form_class = ArtworkForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image=Artwork.objects.get(title='h')
        print(image.image)
        context['form'] = ArtworkForm(initial={'title': 'foo','image':image.image})
        context['artworks'] = Artwork.objects.all()
        return context

class ArtworksUpdateView(UpdateView):
    model = Artwork
    fields = ['title','image','description','catergory','tags']
    template_name='artwork/artwork_update.html'
    success_url = '/artworks/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')


class ArtworksDeleteView(DeleteView):
    model = Artwork
    template_name = 'artwork/artwork_delete_confirmation.html'
    success_url = '/artworks/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')

class TagsListView(ListView):
    model = Tag
    template_name = 'tags/tags_list.html'

class TagsCreateView(CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tags/tag_create.html'
    success_url = '/tags/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')

class TagsUpdateView(UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tags/tag_update.html'
    success_url = '/tags/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')

class TagsDeleteView(DeleteView):
    model = Tag
    template_name = 'tags/tag_delete_confirmation.html'
    success_url = '/tags/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')


class ProductsView(ListView):
    model = Product
    template_name = 'products/product_list.html'

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
    template_name = 'products/product_new.html'
    success_url = '/products/'
    
    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')


class UpdateProductView(UpdateView):
    model = Product
    fields = ['name','image','price','buy_link','catergory','description']
    template_name='products/product_update.html'

    def get_success_url(self):
        return reverse("product_show",kwargs={'pk':self.object.pk})
    
    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/product_delete_confirmation.html'
    success_url = '/products/'

    #check if user is client will send to hompage if not
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.profile.is_client:
                return super().dispatch(request, *args, **kwargs)
        return redirect('/unauthorized/')

class ReviewsCreateView(View):
    def post(self,request):
        if request.user:
            title = request.POST.get('title')
            content = request.POST.get('content')
            user = request.user
            #check if there is not title or content, and if user is authenicated
            if len(title)<1:
                title = 'No Title'
            if len(content)<1:
                content = 'No Content'
            if not request.user.is_authenticated:
                return redirect('/unauthorized/')
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
        if len(title)<1:
            title = 'No Title'
        if len(content)<1:
                content = 'No Content'
        if not request.user.pk == Review.objects.get(pk=pk).user.pk:
            return redirect('/unauthorized/')
        updated_review = Review.objects.filter(pk=pk).update(title=title,content=content)
        return redirect(f'/products/{review.product.pk}')

class ReviewsDeleteView(View):
    def post(self,request,pk):
        review = Review.objects.get(pk=pk)
        if not request.user.pk == Review.objects.get(pk=pk).user.pk:
            return redirect('/unauthorized/')
        Review.objects.filter(pk=pk).delete()
        return redirect(f'/products/{review.product.pk}')

class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs/blogs_list.html'

class BlogsCreateView(CreateView):
    model = Blog
    fields = ['title','content']
    template_name = 'blogs/blog_create.html'
    success_url = '/blogs/'

    #added user to form
    def form_valid(self, form):
        form.instance.user = self.request.user
        super(BlogsCreateView, self).form_valid(form)
        return redirect('/blogs/')

class BlogsUpdateView(UpdateView):
    model = Blog
    fields = ['title','content']
    template_name = 'blogs/blog_update.html'
    success_url = '/blogs/'

class BlogsDeleteView(DeleteView):
    model = Blog
    template_name = 'blogs/blog_delete_confirmation.html'
    success_url = '/blogs/'

class ContactView(TemplateView):
    template_name = 'contact.html'


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        product_pk = request.POST.get('product')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.profile.is_client == True:
                request.session['username'] = username
                request.session['password']= password
                request.session['mfa_code'] = randomCodeGenerator()
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                client.messages.create(to='+16512480589',
                from_='+14086178934',
                body=request.session['mfa_code'])
                print('IS CLIENTDFAS!!')
                return redirect('/mfalogin/')
            login(request, user)
            if product_pk is None:
                return redirect('/')
            return redirect(f'/products/{product_pk}')

        else:
            messages.add_message(request, messages.WARNING, 'The Username or Password was Incorrect')
            if product_pk is None:
                return redirect('/login/')
            return redirect(f'/products/{product_pk}')

class MFAloginView(View):
    def get(self,request):
        return render(request,'mfalogin.html')

    def post(self,request):
        recieved_code = request.POST.get('code')
        if str(recieved_code) == request.session.get('mfa_code'):
            print("MFA LOGIN!!")
            username = request.session.get('username')
            password = request.session.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return redirect('/mfalogin')

class MFAnewcode(View):
    def post(self,request):
        print('HIT')
        request.session['mfa_code'] = randomCodeGenerator()
        print('HIT ROute',request.session['mfa_code'])
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(to='+16512480589',
                from_='+14086178934',
                body=request.session['mfa_code'])
        return redirect('/mfalogin')


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
            Profile.objects.create(user=request.user,is_client=False)
            return redirect(f'/products/{product_pk}')
        else:
            messages.add_message(request, messages.WARNING, form.errors)
            return redirect(f'/products/{product_pk}')

class Broadcast_sms(View):
    def post(self,request):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(to='+16512480589',
                                from_='+14086178934',
                                body='twilio test')
        return HttpResponse("messages sent!", 200)


class UnauthorizedView(TemplateView):
    template_name = 'unauthorized.html'

class HomerenderView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homerender.html'
    
    def get(self, request):
        queryset = Profile.objects.all()
        return Response({'profiles': queryset})


def randomCodeGenerator():
    code = ''
    for i in range(0,3):
        code+=str(randint(1,10))
    print('CODE!!',code)
    return code