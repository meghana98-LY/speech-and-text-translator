from django.db import models
from django.core.validators import FileExtensionValidator

# Audio file validator
AUDIO_EXTENSIONS = ['mp3', 'wav', 'ogg', 'm4a', 'flac']


class AudioFile(models.Model):
    """Model to store uploaded audio files"""
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('hi', 'Hindi'),
        ('ja', 'Japanese'),
        ('zh', 'Chinese'),
    ]
    
    audio_file = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(allowed_extensions=AUDIO_EXTENSIONS)],
        help_text='Supported formats: MP3, WAV, OGG, M4A, FLAC'
    )
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text='Input Language'
    )
    output_language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text='Language to translate to'
    )
    text_output = models.TextField(blank=True, null=True, help_text='Transcribed text from audio')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"Audio - {self.language} - {self.uploaded_at}"


class TextFile(models.Model):
    """Model to store text for TTS conversion"""
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('hi', 'Hindi'),
        ('ja', 'Japanese'),
        ('zh', 'Chinese'),
    ]
    
    text_input = models.TextField(help_text='Text to convert to speech')
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text='Input Language'
    )
    output_language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default='en',
        help_text='Language to translate to'
    )
    translated_text = models.TextField(blank=True, null=True, help_text='Translated text')
    audio_output = models.FileField(
        upload_to='tts/',
        blank=True,
        null=True,
        help_text='Generated audio file'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"TTS - {self.language} - {self.created_at}"
