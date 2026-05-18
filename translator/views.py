from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import AudioFile, TextFile
from .forms import AudioUploadForm, TextToSpeechForm


def home(request):
    """Home page with options for STT and TTS"""
    return render(request, 'home.html')


def speech_to_text(request):
    """Speech-to-Text conversion view"""
    audio_files = AudioFile.objects.all()
    form = AudioUploadForm()
    
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save()
            messages.success(request, 'Audio file uploaded successfully!')
            # TODO: Implement actual STT conversion here
            # For now, just save the file
            return redirect('stt')
    
    context = {
        'form': form,
        'audio_files': audio_files,
        'page_title': 'Speech to Text'
    }
    return render(request, 'stt.html', context)


def text_to_speech(request):
    """Text-to-Speech conversion view"""
    text_files = TextFile.objects.all()
    form = TextToSpeechForm()
    
    if request.method == 'POST':
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            text = form.save()
            messages.success(request, 'Text submitted for conversion!')
            # TODO: Implement actual TTS conversion here
            # For now, just save the text
            return redirect('tts')
    
    context = {
        'form': form,
        'text_files': text_files,
        'page_title': 'Text to Speech'
    }
    return render(request, 'tts.html', context)


def audio_detail(request, pk):
    """View details of a specific audio file"""
    audio = get_object_or_404(AudioFile, pk=pk)
    context = {
        'audio': audio,
        'page_title': f'Audio Detail - {audio.language}'
    }
    return render(request, 'audio_detail.html', context)


def text_detail(request, pk):
    """View details of a specific text file"""
    text = get_object_or_404(TextFile, pk=pk)
    context = {
        'text': text,
        'page_title': f'TTS Detail - {text.language}'
    }
    return render(request, 'text_detail.html', context)


def delete_audio(request, pk):
    """Delete an audio file"""
    audio = get_object_or_404(AudioFile, pk=pk)
    if request.method == 'POST':
        audio.delete()
        messages.success(request, 'Audio file deleted successfully!')
        return redirect('stt')
    return render(request, 'confirm_delete.html', {'object': audio})


def delete_text(request, pk):
    """Delete a text record"""
    text = get_object_or_404(TextFile, pk=pk)
    if request.method == 'POST':
        text.delete()
        messages.success(request, 'Text record deleted successfully!')
        return redirect('tts')
    return render(request, 'confirm_delete.html', {'object': text})
