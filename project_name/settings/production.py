from .base import *
import dj_database_url
from os import environ
from urllib.parse import urlparse
from django.conf import global_settings

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = get_env_variable('SECRET_TOKEN')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# https://docs.djangoproject.com/en/1.8/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allowed hosts
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-STATICFILES_STORAGE
STATICFILES_STORAGE = global_settings.STATICFILES_STORAGE

# MAIL CONFIGURATION
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.sendgrid.net')
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-host-user
EMAIL_HOST_USER = get_env_variable('SENDGRID_USERNAME')
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_env_variable('SENDGRID_PASSWORD')
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
# https://docs.djangoproject.com/en/1.8/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# CACHE CONFIGURATION
# https://docs.djangoproject.com/en/1.8/ref/settings/#caches
redis_url = urlparse(get_env_variable('REDISTOGO_URL'))
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': redis_url.password,
        }
    }
}

# celery
# http://celery.readthedocs.org/en/latest/configuration.html#broker-url
BROKER_URL = get_env_variable('CLOUDAMQP_URL')
# http://celery.readthedocs.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'redis'
