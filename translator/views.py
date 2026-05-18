from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.files import File
from django.conf import settings
import os
import speech_recognition as sr
import librosa
import soundfile as sf
from gtts import gTTS
from deep_translator import GoogleTranslator

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
            
            try:
                audio_path = audio.audio_file.path
                
                # Convert to WAV if it's not WAV, as SpeechRecognition works best with WAV
                if not audio_path.lower().endswith('.wav'):
                    y, sr_rate = librosa.load(audio_path, sr=None)
                    wav_path = audio_path + '.wav'
                    sf.write(wav_path, y, sr_rate)
                    recognizer_path = wav_path
                else:
                    wav_path = None
                    recognizer_path = audio_path
                    
                r = sr.Recognizer()
                with sr.AudioFile(recognizer_path) as source:
                    audio_data = r.record(source)
                    
                # The model uses 'en', 'es', 'fr', etc. Google SR uses BCP-47
                lang_mapping = {
                    'en': 'en-US', 'es': 'es-ES', 'fr': 'fr-FR', 'de': 'de-DE',
                    'hi': 'hi-IN', 'ja': 'ja-JP', 'zh': 'zh-CN'
                }
                locale = lang_mapping.get(audio.language, 'en-US')
                
                text = r.recognize_google(audio_data, language=locale)
                
                # Deep-translator mapping (zh needs to be zh-CN)
                dt_map = {'zh': 'zh-CN'}
                src_lang = dt_map.get(audio.language, audio.language)
                tgt_lang = dt_map.get(audio.output_language, audio.output_language)
                
                # Translate the recognized text
                translator = GoogleTranslator(source=src_lang, target=tgt_lang)
                translated_text = translator.translate(text)
                
                audio.text_output = translated_text
                audio.save()
                
                if wav_path and os.path.exists(wav_path):
                    os.remove(wav_path)
                    
                messages.success(request, 'Audio file transcribed and translated successfully!')
            except Exception as e:
                messages.error(request, f'STT Error: Could not transcribe/translate the audio. {str(e)}')

            return redirect('translator:stt')
    
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
            text_obj = form.save()
            
            try:
                # Deep-translator mapping (zh needs to be zh-CN)
                dt_map = {'zh': 'zh-CN'}
                src_lang = dt_map.get(text_obj.language, text_obj.language)
                tgt_lang = dt_map.get(text_obj.output_language, text_obj.output_language)
                
                # Translate text first
                translator = GoogleTranslator(source=src_lang, target=tgt_lang)
                translated_text = translator.translate(text_obj.text_input)
                
                # Save the translated text so it can be displayed
                text_obj.translated_text = translated_text
                text_obj.save()
                
                # Use gTTS for generating speech with the translated text and output language
                tts = gTTS(text=translated_text, lang=tgt_lang, slow=False)
                
                # Make sure MEDIA_ROOT/tts exists
                os.makedirs(os.path.join(settings.MEDIA_ROOT, 'tts'), exist_ok=True)
                
                temp_filename = f"tts_temp_{text_obj.pk}.mp3"
                temp_path = os.path.join(settings.MEDIA_ROOT, 'tts', temp_filename)
                
                tts.save(temp_path)
                
                with open(temp_path, 'rb') as f:
                    final_filename = f"tts_{text_obj.pk}_{text_obj.output_language}.mp3"
                    text_obj.audio_output.save(final_filename, File(f), save=True)
                
                os.remove(temp_path)
                messages.success(request, 'Text translated and converted to speech successfully!')
            except Exception as e:
                messages.error(request, f'TTS Error: Could not translate/generate speech. {str(e)}')
                
            return redirect('translator:tts')
    
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
        return redirect('translator:stt')
    return render(request, 'confirm_delete.html', {'object': audio})


def delete_text(request, pk):
    """Delete a text record"""
    text = get_object_or_404(TextFile, pk=pk)
    if request.method == 'POST':
        text.delete()
        messages.success(request, 'Text record deleted successfully!')
        return redirect('translator:tts')
    return render(request, 'confirm_delete.html', {'object': text})
