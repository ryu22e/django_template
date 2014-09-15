django_template
===============

A project template for Django 1.7.

Installation
------------

django_template supports Django 1.7.x and Python 3.4.x.

To create a new django_template base project, run the following command (this assumes you have Django 1.7.x installed already)::

    django-admin.py startproject --template=https://github.com/ryu22e/django_template/archive/master.zip --extension=json,py,rst your_project
    cd your_project
    pip install -r requirements/local.txt
    python manage.py syncdb --noinput
    python manage.py runserver
