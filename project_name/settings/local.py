from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'default.db'),
    }
}

INSTALLED_APPS += (
    # celery
    'kombu.transport.django',
    # django-debug-toolbar
    'debug_toolbar.apps.DebugToolbarConfig',
)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1',)
# Tell the toolbar not to adjust your settings automatically by adding this line in your settings module
DEBUG_TOOLBAR_PATCH_SETTINGS = False


# MAIL CONFIGURATION
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CACHE CONFIGURATION
# https://docs.djangoproject.com/en/1.8/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# celery
# http://celery.readthedocs.org/en/latest/configuration.html#broker-url
BROKER_URL = environ.get('BROKER_URL', 'django://')
# http://celery.readthedocs.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'db+sqlite:///' + os.path.join(BASE_DIR, 'celery.db')
# http://celery.readthedocs.org/en/latest/configuration.html#celery-redirect-stdouts-level
CELERY_REDIRECT_STDOUTS_LEVEL = 'DEBUG'
