#!/bin/sh

gunicorn blog.wsgi:application -b 0.0.0.0:8000 --reload
