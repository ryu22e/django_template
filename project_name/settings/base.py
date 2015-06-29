"""
Django settings for {{ project_name }} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os import environ
from os.path import dirname, normpath, abspath, join
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

# Path Configuration
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = '{{ secret_key }}'


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
# Apps specific for this project go here.
LOCAL_APPS = (
    'home',
)
INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = 'wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

# Static directories
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

# Staticfiles finders
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# Media files
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

# Templates configuration
# https://docs.djangoproject.com/en/1.8/topics/templates/#configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates')),
        ],
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

# celery
# http://celery.readthedocs.org/en/latest/configuration.html#celery-task-serializer
CELERY_TASK_SERIALIZER = 'json'
# http://celery.readthedocs.org/en/latest/configuration.html#celery-result-serializer
CELERY_RESULT_SERIALIZER = 'json'
# http://celery.readthedocs.org/en/latest/configuration.html#celery-accept-content
CELERY_ACCEPT_CONTENT = ['json']
# http://celery.readthedocs.org/en/latest/configuration.html#std:setting-CELERYBEAT_SCHEDULE
CELERYBEAT_SCHEDULE = {
    #'add-every-30-seconds': {
    #    'task': 'example.tasks.add',
    #    'schedule': timedelta(seconds=30),
    #    'args': (16, 16),
    #},
}
