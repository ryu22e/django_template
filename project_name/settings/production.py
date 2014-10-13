from .base import *
import dj_database_url
from os import environ

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

# Allowed hosts
# https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

# django-celery
INSTALLED_APPS += ('djcelery', )
# http://docs.celeryproject.org/en/latest/configuration.html#broker-transport
BROKER_TRANSPORT = 'amqplib'
# Set this number to the amount of allowed concurrent connections on your AMQP
# provider, divided by the amount of active workers you have.
#
# For example, if you have the 'Little Lemur' CloudAMQP plan (their free tier),
# they allow 3 concurrent connections. So if you run a single worker, you'd
# want this number to be 3. If you had 3 workers running, you'd lower this
# number to 1, since 3 workers each maintaining one open connection = 3
# connections total.
#
# http://docs.celeryproject.org/en/latest/configuration.html#broker-pool-limit
BROKER_POOL_LIMIT = 3
# http://docs.celeryproject.org/en/latest/configuration.html#broker-connection-max-retries
BROKER_CONNECTION_MAX_RETRIES = 0
# http://docs.celeryproject.org/en/latest/configuration.html#broker-url
BROKER_URL = environ.get('RABBITMQ_URL', environ.get('CLOUDAMQP_URL'))
# http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend
CELERY_RESULT_BACKEND = 'amqp'

# MAIL CONFIGURATION
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.sendgrid.net')
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-host-user
EMAIL_HOST_USER = get_env_variable('SENDGRID_USERNAME')
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_env_variable('SENDGRID_PASSWORD')
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
# https://docs.djangoproject.com/en/1.7/ref/settings/#email-use-tls
EMAIL_USE_TLS = True