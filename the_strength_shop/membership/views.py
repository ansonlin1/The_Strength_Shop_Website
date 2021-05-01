from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MembershipHomePage(TemplateView):
    template_name = "membership/membership_home.html"
