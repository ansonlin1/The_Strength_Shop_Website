from django.urls import path, include
from . import views

app_name = 'apparel'

urlpatterns = [
    path('', views.ApparelListPage.as_view(), name='apparel_list'),
]
