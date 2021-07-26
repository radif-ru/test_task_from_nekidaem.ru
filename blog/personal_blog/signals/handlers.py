from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.urls import reverse_lazy

from blog.settings import DOMAIN_NAME, EMAIL_HOST_USER
from personal_blog.models import UserPost, UserSubscribeBlog


@receiver(post_save, sender=UserPost)
def forwarding_to_save(sender, instance, **kwargs):
    email_sender(instance, 'появился/обновился')


@receiver(pre_delete, sender=UserPost)
def forwarding_to_delete(sender, instance, **kwargs):
    email_sender(instance, 'удалён')


def email_sender(instance, text):
    if instance.pk:
        post_link = reverse_lazy(
            'post-page',
            kwargs={
                'pk': instance.id
            }
        )

        subscriptions = UserSubscribeBlog.objects.filter(
            author_blog=instance.user)
        recipient_list = [sub.user.email for sub in subscriptions]

        title = f'У {instance.user.username} {text} пост'

        message = f'В блоге пользователя {instance.user.username} ' \
                  f'{text} пост. Смотрите сами:\n' \
                  f'{DOMAIN_NAME}{post_link}'

        send_mail(
            title, message, EMAIL_HOST_USER, recipient_list,
            fail_silently=False
        )
