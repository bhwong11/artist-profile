from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('artworks/new/',views.ArtworkView.as_view(),name='create'),
    path('artworks/',views.ArtworksView.as_view(),name='artworks'),
    path('products/',views.ProductsView.as_view(),name='products'),
    path('products/new',views.ProductsCreateView.as_view(),name='product_new'),
    path('products/<int:pk>/',views.ProductShowView.as_view(),name='product_show'),
    path('products/<int:pk>/update/',views.UpdateProductView.as_view(),name='product_update'),
    path('products/<int:pk>/delete/',views.DeleteProductView.as_view(),name='product_delete'),
]