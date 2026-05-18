from django.contrib import admin
from .models import AudioFile, TextFile


@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'uploaded_at', 'has_text_output']
    list_filter = ['language', 'uploaded_at']
    search_fields = ['text_output']
    readonly_fields = ['uploaded_at']
    
    def has_text_output(self, obj):
        return bool(obj.text_output)
    has_text_output.boolean = True
    has_text_output.short_description = 'Has Transcription'


@admin.register(TextFile)
class TextFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'language', 'text_preview', 'has_audio_output', 'created_at']
    list_filter = ['language', 'created_at']
    search_fields = ['text_input']
    readonly_fields = ['created_at']
    
    def text_preview(self, obj):
        return obj.text_input[:50] + '...' if len(obj.text_input) > 50 else obj.text_input
    text_preview.short_description = 'Text'
    
    def has_audio_output(self, obj):
        return bool(obj.audio_output)
    has_audio_output.boolean = True
    has_audio_output.short_description = 'Has Audio'
