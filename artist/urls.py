from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('artworks/new/',views.ArtworkView.as_view(),name='create'),
    path('artworks/',views.ArtworksView.as_view(),name='artworks'),
    path('artworks/<int:pk>/update',views.ArtworksUpdateView.as_view(),name='artwork_update'),
    path('artworks/<int:pk>/delete',views.ArtworksDeleteView.as_view(),name='artwork_delete'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('products/new',views.ProductsCreateView.as_view(),name='product_new'),
    path('products/<int:pk>/',views.ProductShowView.as_view(),name='product_show'),
    path('products/<int:pk>/update/',views.UpdateProductView.as_view(),name='product_update'),
    path('products/<int:pk>/delete/',views.DeleteProductView.as_view(),name='product_delete'),
    path('reviews/new/',views.ReviewsCreateView.as_view(),name='review_new'),
    path('reviews/<int:pk>/update/',views.ReviewsUpdateView.as_view(),name='review_update'),
    path('reviews/<int:pk>/delete/',views.ReviewsDeleteView.as_view(),name='review_delete'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
]