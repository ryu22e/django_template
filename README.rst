django_template
===============

A project template for Django 1.8.x.

.. image:: https://circleci.com/gh/ryu22e/django_template.svg?style=svg
    :target: https://circleci.com/gh/ryu22e/django_template

Installation
------------

django_template supports Django 1.8.x and Python 3.5.x.

To create a new django_template base project, run the following command (this assumes you have Django 1.8.x installed already)::

    django-admin.py startproject --template=https://github.com/ryu22e/django_template/archive/master.zip --extension=json,py,rst your_project
    cd your_project
    pip install -U pip
    pip install -r requirements/local.txt
    python manage.py migrate --noinput
    python manage.py runserver

Updating Python packages
------------------------

To update python packages, run the following command::

    cd /path/to/your_project
    invoke pip_compile_all

Running tests
-------------

To run tests, run the following command::

    cd /path/to/your_project
    python manage.py test --settings your_project.settings.test


Deploying to Heroku
-------------------

If you want to deploy to `Heroku <https://www.heroku.com/>`_, run the following command::

    cd /path/to/your_project
    rm circle.yml
    git init
    git add .
    git commit -am "Initial commit"

    heroku apps:create your_project
    heroku addons:create heroku-postgresql
    heroku addons:create scheduler
    heroku addons:create cloudamqp
    heroku addons:create newrelic
    heroku addons:create papertrail
    heroku addons:create sendgrid
    heroku addons:create process-scheduler
    heroku addons:create redistogo
    heroku config:add DJANGO_SETTINGS_MODULE="your_project.settings.production"
    heroku config:add SECRET_TOKEN="<A secret key for verifying the integrity of signed cookies.>"
    heroku config:add WEB_CONCURRENCY=4
    heroku config:add CELERY_APP=your_project
    heroku config:add NEW_RELIC_APP_NAME=your_project

    git push heroku master
    heroku run "python manage.py migrate --noinput"

    heroku open

You can also add `Heroku Button <https://blog.heroku.com/archives/2014/8/7/heroku-button>`_ to README file.

Markdown snippet::

    [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

reStructuredText snippet::

   .. image:: https://www.herokucdn.com/deploy/button.png
     :alt: Deploy
     :target: https://heroku.com/deploy
