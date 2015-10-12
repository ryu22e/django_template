from .base import *  # NOQA
import logging

# Disable logging, Because this doesn't need to run tests.
logging.disable(logging.CRITICAL)

# Disable Debug mode, Because this doesn't need to run tests.
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.db'),
    }
}

# celery
# http://docs.celeryproject.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True
