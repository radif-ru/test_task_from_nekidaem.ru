import os
import json

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from blog.settings import JSON_PATH
from personalblogapp.models import UserPost


def load_from_json(file_name: str) -> dict:
    """загружает данные из json файла, дампа талицы, возвращает словарь"""
    with open(
            os.path.join(JSON_PATH, f'{file_name}.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        if not get_user_model().objects.exists():
            get_user_model().objects.create_superuser(
                username='radif',
                email='mail@radif.ru',
                password='qwertytrewq')

            get_user_model().objects.create_user(
                username='Kolya',
                email='kolya@blog.local',
                password='qwertytrewq')

            get_user_model().objects.create_user(
                username='Alyosha',
                email='alyosha@blog.local',
                password='qwertytrewq')

            os.system('python manage.py makemigrations')
            os.system('python manage.py migrate --run-syncdb')

        # создание постов с привязкой к конкретным пользователям,
        # которые были созданы выше, по внешним ключам
        posts = load_from_json('personalblogapp_userpost')
        if not UserPost.objects.exists():
            UserPost.objects.all().delete()
            for post in posts:
                user_name = post['fields']['user']
                _user = get_user_model().objects.get(id=user_name)
                post['fields']['user'] = _user

                new_publication = UserPost(**{'id': post['pk']},
                                           **post['fields'])
                new_publication.save()

        # сброс последовательностей в базе данных
        sequence_sql = connection.ops.sequence_reset_sql(
            no_style(), [UserPost, get_user_model()])
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)
