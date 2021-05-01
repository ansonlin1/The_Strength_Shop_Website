from django.urls import path, include
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.SendEmail, name='about_home'),
]
