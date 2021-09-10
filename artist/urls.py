from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('artworks/new/',views.ArtworkCreateView.as_view(),name='artwork_create'),
    path('artworks/',views.ArtworksView.as_view(),name='artworks'),
    path('artworks/<int:pk>/update',views.ArtworksUpdateView.as_view(),name='artwork_update'),
    path('artworks/<int:pk>/delete',views.ArtworksDeleteView.as_view(),name='artwork_delete'),
    path('tags/',views.TagsListView.as_view(),name='tags'),
    path('tags/new',views.TagsCreateView.as_view(),name='tag_new'),
    path('tags/<int:pk>/update',views.TagsUpdateView.as_view(),name='tag_update'),
    path('tags/<int:pk>/delete',views.TagsDeleteView.as_view(),name='tag_delete'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('products/new',views.ProductsCreateView.as_view(),name='product_new'),
    path('products/<int:pk>/',views.ProductShowView.as_view(),name='product_show'),
    path('products/<int:pk>/update/',views.UpdateProductView.as_view(),name='product_update'),
    path('products/<int:pk>/delete/',views.DeleteProductView.as_view(),name='product_delete'),
    path('reviews/new/',views.ReviewsCreateView.as_view(),name='review_new'),
    path('reviews/<int:pk>/update/',views.ReviewsUpdateView.as_view(),name='review_update'),
    path('reviews/<int:pk>/delete/',views.ReviewsDeleteView.as_view(),name='review_delete'),
    path('blogs/',views.BlogsListView.as_view(),name='blogs'),
    path('blogs/new',views.BlogsCreateView.as_view(),name='blog_new'),
    path('blogs/<int:pk>/update',views.BlogsUpdateView.as_view(),name='blog_update'),
    path('blogs/<int:pk>/delete',views.BlogsDeleteView.as_view(),name='blog_delete'),
    path('contact',views.ContactView.as_view(),name='contact'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('homerender/',views.HomerenderView.as_view(),name='homerender'),
    path('broadcast/', views.Broadcast_sms.as_view(), name="broadcast"),
    path('mfalogin/', views.MFAloginView.as_view(), name="mfalogin"),
    path('newmfacode/', views.MFAnewcode.as_view(), name="newmfacode"),
    path('unauthorized/',views.UnauthorizedView.as_view(),name='unauthorized'),
]