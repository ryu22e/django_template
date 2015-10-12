from .base import *  # NOQA
import logging

# Disable logging, Because this doesn't need to run tests.
logging.disable(logging.CRITICAL)

# Disable Debug mode, Because this doesn't need to run tests.
DEBUG = False

INSTALLED_APPS += (
    'django_jenkins',
)

PROJECT_APPS = LOCAL_APPS

JENKINS_TASKS = (
    'django_jenkins.tasks.run_flake8',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

# celery
# http://docs.celeryproject.org/en/latest/configuration.html#celery-always-eager
CELERY_ALWAYS_EAGER = True

# Use fastest hasher to speed up tests.
# SECURITY WARNING: don't use this hasher in production!
# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-PASSWORD_HASHERS
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
