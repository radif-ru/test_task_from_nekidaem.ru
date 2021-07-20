import os
import json

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

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

        os.system('python manage.py makemigrations')
        os.system('python manage.py migrate --run-syncdb')

        get_user_model().objects.all().delete()

        if not get_user_model().objects.filter(username='admin').exists():
            get_user_model().objects.create_superuser(
                username='radif',
                email='mail@radif.ru',
                password='qwertytrewq')

        if not get_user_model().objects.filter(username='user').exists():
            get_user_model().objects.create_user(
                username='Kolya',
                email='kolya@blog.local',
                password='qwertytrewq')

        if not get_user_model().objects.filter(username='user2').exists():
            get_user_model().objects.create_user(
                username='Alyosha',
                email='alyosha@blog.local',
                password='qwertytrewq')

        posts = load_from_json('personalblogapp_userpost')
        UserPost.objects.all().delete()
        for post in posts:
            user_name = post['fields']['user']
            _user = get_user_model().objects.get(id=user_name)
            post['fields']['user'] = _user

            new_publication = UserPost(**{'id': post['pk']}, **post['fields'])
            new_publication.save()