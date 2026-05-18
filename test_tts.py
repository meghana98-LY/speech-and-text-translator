import os
from deep_translator import GoogleTranslator
from gtts import gTTS

print("Testing Spanish")
try:
    translated_es = GoogleTranslator(source='en', target='es').translate('hello world')
    print("Translated (es):", translated_es)
    tts_es = gTTS(text=translated_es, lang='es', slow=False)
    tts_es.save('test_es.mp3')
    print("TTS (es) saved.")
except Exception as e:
    print("Error ES:", e)

print("Testing French")
try:
    translated_fr = GoogleTranslator(source='en', target='fr').translate('hello world')
    print("Translated (fr):", translated_fr)
    tts_fr = gTTS(text=translated_fr, lang='fr', slow=False)
    tts_fr.save('test_fr.mp3')
    print("TTS (fr) saved.")
except Exception as e:
    print("Error FR:", e)

print("Testing Chinese")
try:
    translated_zh = GoogleTranslator(source='en', target='zh-CN').translate('hello world')
    print("Translated (zh):", translated_zh)
    tts_zh = gTTS(text=translated_zh, lang='zh-CN', slow=False)
    tts_zh.save('test_zh.mp3')
    print("TTS (zh) saved.")
except Exception as e:
    print("Error ZH:", e)
