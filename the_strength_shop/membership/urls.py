from django.urls import path, include
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipHomePage.as_view(), name='membership_home'),
]
