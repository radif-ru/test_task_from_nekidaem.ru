#! /bin/bash

python manage.py collectstatic

python manage.py makemigrations
python manage.py migrate
python manage.py fill_db

#python manage.py makemigrations --no-input
#python manage.py migrate --no-input

gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload
