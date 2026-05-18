from django.urls import path
from . import views

app_name = 'translator'

urlpatterns = [
    path('', views.home, name='home'),
    
    # Speech to Text routes
    path('stt/', views.speech_to_text, name='stt'),
    path('audio/<int:pk>/', views.audio_detail, name='audio_detail'),
    path('audio/<int:pk>/delete/', views.delete_audio, name='delete_audio'),
    
    # Text to Speech routes
    path('tts/', views.text_to_speech, name='tts'),
    path('text/<int:pk>/', views.text_detail, name='text_detail'),
    path('text/<int:pk>/delete/', views.delete_text, name='delete_text'),
]
