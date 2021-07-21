#! /bin/bash

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py fill_db

#python manage.py collectstatic --no-input

#python gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload

python manage.py runserver 0.0.0.0:8000
