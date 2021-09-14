from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.app, name='twilio'),
    re_path(r'^token', views.token, name='token'),
    re_path(r'^userJoin', views.userJoin, name='token'),
    re_path(r'^userLeaves', views.userLeaves, name='token'),
]