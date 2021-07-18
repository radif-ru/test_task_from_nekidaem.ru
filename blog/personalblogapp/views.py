from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView

from personalblogapp.forms import ReadPostForm
from personalblogapp.models import UserSubscribeBlog, UserPost, ReadPost


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


class ReadPostView(View):
    model = ReadPost
    success_url = reverse_lazy('personalblogapp/index.html')

    def post(self, request, *args, **kwargs):
        post_pk = request.POST.get('read', '')
        if post_pk:
            try:
                ReadPost.objects.get(
                    user_id=request.user, post_id=post_pk).delete()
            except ReadPost.DoesNotExist as e:
                ReadPost.objects.create(
                    user_id=request.user.pk, post_id=post_pk)
        return HttpResponseRedirect('/')
