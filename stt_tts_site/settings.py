from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6!o2*3*t2zc8y=l&3nej%joo+wrnkb&qchc9m@jngq*uowzqbw'

DEBUG = True

ALLOWED_HOSTS = []   # later add domain/IP when deploying


# -------------------- Installed Apps --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'translator',      #  <-- renamed app
]


# -------------------- Middleware --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'stt_tts_site.urls'


# -------------------- Templates --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],                     # we use app templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'stt_tts_site.wsgi.application'


# -------------------- Database --------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------- Password Validators --------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# -------------------- Internationalization --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# -------------------- Static Files --------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",           # for your custom static files
]
STATIC_ROOT = BASE_DIR / "staticfiles"   # created auto when deploying


# -------------------- Media (IMPORTANT for audio files) --------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'    # uploaded + generated audio saved here


# -------------------- Default Primary Key --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
