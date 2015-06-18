web: newrelic-admin run-program gunicorn --workers $WEB_CONCURRENCY wsgi --log-file -
scheduler: celery beat -A $CELERY_APP_NAME -l info
worker: celery worker -A $CELERY_APP_NAME -l info
