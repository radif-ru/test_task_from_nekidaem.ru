#! /bin/bash

#python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
python manage.py fill_db

gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload
