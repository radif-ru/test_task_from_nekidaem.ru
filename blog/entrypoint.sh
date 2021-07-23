#! /bin/bash

#if [ "$DATABASE" = "postgres" ]
#then
#    echo "Waiting for postgres..."
#
#    while ! nc -z $SQL_HOST $SQL_PORT; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started"
#fi

#python manage.py collectstatic

python manage.py flush --no-input

#python manage.py makemigrations
python manage.py migrate
python manage.py fill_db

gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload

#exec "$@"