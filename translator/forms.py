from django import forms
from .models import AudioFile, TextFile


class AudioUploadForm(forms.ModelForm):
    """Form for uploading audio files for STT"""
    
    class Meta:
        model = AudioFile
        fields = ['audio_file', 'language', 'output_language']
        widgets = {
            'audio_file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'audio/*',
            }),
            'language': forms.Select(attrs={
                'class': 'form-control',
            }),
            'output_language': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class TextToSpeechForm(forms.ModelForm):
    """Form for entering text for TTS conversion"""
    
    class Meta:
        model = TextFile
        fields = ['text_input', 'language', 'output_language']
        widgets = {
            'text_input': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter text to convert to speech...',
            }),
            'language': forms.Select(attrs={
                'class': 'form-control',
            }),
            'output_language': forms.Select(attrs={
                'class': 'form-control',
            }),
        }
