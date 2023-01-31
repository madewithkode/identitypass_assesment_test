from identitypass_interview_test.settings.base import *
import os

from dotenv import load_dotenv

load_dotenv()

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('POSTGRES_HOST'),
        'USER': os.environ.get('POSTGRES_USER'),
        'NAME': os.environ.get('POSTGRES_DB'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'PORT': 5432,
    },
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
  'http://localhost:8887',
  'http://127.0.0.1:8887',
  'http://localhost:5500',
  'http://127.0.0.1:5500'
)

ALLOWED_HOSTS=['*']

BACKEND_URL = 'http://localhost:8000'

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

