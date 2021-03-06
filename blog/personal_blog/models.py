from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class UserPost(models.Model):
    user = models.ForeignKey(
        USER, verbose_name='пользователь', on_delete=models.CASCADE
    )
    title = models.CharField(verbose_name='заголовок', max_length=50)
    text = models.TextField(verbose_name='текст', blank=False)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def __str__(self):
        return f'Автор - {self.user} | ' \
               f'Заголовок - {self.title[:15]} | ' \
               f'Текст - {self.text[:30]}...'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-updated']


class ReadPost(models.Model):
    user = models.ForeignKey(
        USER, verbose_name='пользователь', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        UserPost, verbose_name='прочитал пост', on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Пользователь - {self.user} | ' \
               f'Прочитал пост пользователя - {self.post.user} | ' \
               f'Заголовок - {self.post.title} | ' \
               f'Текст - {self.post.text[:15]}...'

    class Meta:
        verbose_name = 'прочитанный пост'
        verbose_name_plural = 'прочитанные посты'
        unique_together = (('user', 'post'),)


class UserSubscribeBlog(models.Model):
    user = models.ForeignKey(
        USER, verbose_name='пользователь', on_delete=models.CASCADE
    )
    author_blog = models.ForeignKey(
        USER, verbose_name='чей блог',
        on_delete=models.CASCADE, related_name='author_blog'
    )

    def __str__(self):
        return f'Пользователь - {self.user} | ' \
               f'Подписан на блог пользователя - {self.author_blog}. '

    class Meta:
        verbose_name = 'пользователь подписан на блог автора'
        verbose_name_plural = 'пользователи подписаны на блоги авторов'
        unique_together = (('user', 'author_blog'),)
