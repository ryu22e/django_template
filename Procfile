web: newrelic-admin run-program gunicorn --workers $WEB_CONCURRENCY django_template.wsgi --log-file -
scheduler: python manage.py celery worker -B -E --maxtasksperchild=1000
worker: python manage.py celery worker -E --maxtasksperchild=1000