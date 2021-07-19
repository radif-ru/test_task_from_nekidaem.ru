import re
from django import template
from django.conf import settings

from personalblogapp.models import ReadPost

register = template.Library()


@register.filter(name='is_read')
def is_read(post_pk: int, request_user_pk: int) -> str:
    """Проверяет прочитан ли пост"""
    try:
        ReadPost.objects.get(
            user_id=request_user_pk,
            post_id=post_pk)
        return 'прочитан'
    except ReadPost.DoesNotExist as e:
        return 'не_прочитан'
