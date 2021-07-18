from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView

from personalblogapp.models import UserSubscribeBlog, UserPost


class NewsFeed(ListView):
    template_name = 'personalblogapp/index.html'
    model = UserSubscribeBlog
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'лента новостей'
        context['posts'] = self.get_subscriptions()
        return context

    def get_subscriptions(self):
        subscriptions = self.model.objects.filter(user=self.request.user)
        return UserPost.objects.filter(
            user__in=[subscribe.author_blog.pk for subscribe in subscriptions]
        )
