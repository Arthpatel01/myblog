from django.urls import path

from blog import views

urlpatterns = [
    path('', views.Index, name='dashboard'),
]