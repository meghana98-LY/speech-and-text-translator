# STT/TTS Translator

A Django-based web application for Speech-to-Text (STT) and Text-to-Speech (TTS) conversion with support for multiple languages.

## Features

- 🎙️ **Speech to Text**: Convert audio files to text with support for multiple languages
- 🔊 **Text to Speech**: Convert text to natural-sounding audio in multiple languages
- 📁 **Multiple Audio Formats**: Support for MP3, WAV, OGG, M4A, FLAC
- 🌍 **Multi-language Support**: English, Spanish, French, German, Hindi, Japanese, Chinese
- 💾 **File Management**: Upload, view, download, and delete audio/text files
- 🎨 **Modern UI**: Bootstrap 5 responsive design with smooth interactions

## Requirements

- Python 3.8+
- Django 4.2.11
- SQLite3 (included with Python)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd translator
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Usage

### Admin Panel

Access the Django admin panel at `http://localhost:8000/admin/` with your superuser credentials to:
- View and manage audio files
- View and manage text conversions
- Monitor all conversions

### Web Interface

1. **Speech to Text**:
   - Navigate to Speech to Text
   - Upload an audio file
   - Select the language
   - View transcribed text

2. **Text to Speech**:
   - Navigate to Text to Speech
   - Enter your text
   - Select the language
   - Download generated audio

## Project Structure

```
translator/
├── translator/              # Django app
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── urls.py            # URL routing
│   ├── views.py           # View functions
│   └── __init__.py        # Package init
├── stt_tts_site/          # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── media/                 # User uploaded files
│   ├── uploads/          # Uploaded audio files
│   └── tts/             # Generated TTS files
├── static/               # Static files (CSS, JS, images)
├── db.sqlite3           # SQLite database
├── manage.py            # Django CLI
└── requirements.txt     # Python dependencies
```

## Models

### AudioFile
- Stores uploaded audio files
- Tracks language and transcription
- Supports multiple audio formats

### TextFile
- Stores text for TTS conversion
- Tracks language selection
- Links to generated audio files

## Configuration

### Settings

Edit `stt_tts_site/settings.py` to configure:
- `DEBUG = True` (set to False for production)
- `ALLOWED_HOSTS` (add your domain/IP)
- `DATABASES` (use production database for deployment)
- `SECRET_KEY` (use environment variable in production)

### Environment Variables

For production, create a `.env` file:

```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://...
```

## API Endpoints

- `GET /` - Home page
- `GET/POST /stt/` - Speech to Text page
- `GET /audio/<id>/` - Audio file details
- `POST /audio/<id>/delete/` - Delete audio file
- `GET/POST /tts/` - Text to Speech page
- `GET /text/<id>/` - Text details
- `POST /text/<id>/delete/` - Delete text record
- `GET /admin/` - Admin panel

## Deployment

### Using Gunicorn

```bash
gunicorn stt_tts_site.wsgi:application --bind 0.0.0.0:8000
```

### Using Heroku

1. Create `Procfile`:
```
web: gunicorn stt_tts_site.wsgi:application
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Errors
```bash
python manage.py migrate --run-syncdb
```

### Static Files Not Loading
```bash
python manage.py collectstatic
```

## Future Enhancements

- [ ] Real-time STT conversion (WebSocket support)
- [ ] Advanced TTS voice options
- [ ] Batch processing
- [ ] API endpoints for external integration
- [ ] User authentication and per-user file management
- [ ] Cloud storage integration (AWS S3, Google Cloud)
- [ ] Enhanced audio quality options
- [ ] Translation features

## License

MIT License - See LICENSE file for details

## Support

For issues and questions, please create an issue in the repository.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

