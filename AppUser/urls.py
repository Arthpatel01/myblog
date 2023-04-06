from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView

from AppUser import views

urlpatterns = [
    path('userview/', views.userview, name='users'),
]