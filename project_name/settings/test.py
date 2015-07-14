from .base import *  # NOQA

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
