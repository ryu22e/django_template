from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

# Allowed hosts
# https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

DATABASES = {}
DATABASES['default'] = dj_database_url.config()