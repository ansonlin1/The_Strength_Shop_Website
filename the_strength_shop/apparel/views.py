from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class ApparelListPage(TemplateView):
    template_name = "apparel/apparel_list.html"
