from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogHomePage.as_view(), name='blog_home'),
]
