from django.urls import path

from blog import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact-us', views.Contact.as_view(), name='contact-us'),
    path('about-us', views.About.as_view(), name='about-us'),
    path('post-detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_view'),

]