from django.urls import path

from AppTools import views

urlpatterns = [
    path('text_to_speech/', views.TextToSpeech.as_view(), name='text_to_speech'),
]