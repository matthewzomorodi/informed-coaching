"""
Django settings for informedcoaching project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

import environ
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Configure environment variables. Interpolate for Bash-style config
# to ensure configuration of database variables in environment file.
env = environ.Env(interpolate=True)

# By default, django-environ uses existing values of environment variables,
# if they exist, so explicitly set the environment with the values defined
# in the .env file. This also requires that the .env file explicitly set
# variables with null values to ensure defaults defined here are used.
environ.Env.read_env(os.path.join(BASE_DIR, '.env'), overwrite=True)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'practice.apps.PracticeConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'informedcoaching.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'informedcoaching.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_DEFAULT_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': env.str('DB_DEFAULT_NAME', default=BASE_DIR / 'db.sqlite3'),
        'USER': env.str('DB_DEFAULT_USER', default=''),
        'PASSWORD': env.str('DB_DEFAULT_PASSWORD', default=''),
        'HOST': env.str('DB_DEFAULT_HOST', default=''),
        'PORT': env.str('DB_DEFAULT_PORT', default='')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Destination folder for collectstatic command
STATIC_ROOT = env.str('STATIC_ROOT', default='')

STATIC_URL = env.str('STATIC_URL', default='static/')

# Media files (i.e. User uploaded files)
# https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-MEDIA_ROOT
# https://docs.djangoproject.com/en/5.0/howto/static-files/
# https://docs.djangoproject.com/en/5.0/ref/views/#serving-files-in-development
# https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/

# Absolute filesystem path to the directory that will hold user-uploaded files
MEDIA_ROOT = env.str('MEDIA_ROOT', default=os.path.join(BASE_DIR.parent, 'media/'))

MEDIA_URL= env.str('MEDIA_URL', 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'