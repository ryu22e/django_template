web: newrelic-admin run-program gunicorn --workers $WEB_CONCURRENCY wsgi --log-file -
scheduler: celery beat -l info
worker: celery worker -l info
