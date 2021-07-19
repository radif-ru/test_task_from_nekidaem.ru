from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from blog.settings import LOGIN_REDIRECT_URL
from personalblogapp.forms import ReadPostForm
from personalblogapp.models import UserSubscribeBlog, UserPost, ReadPost


class NewsFeed(ListView):
    template_name = 'personalblogapp/index.html'
    model = UserSubscribeBlog
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'лента новостей'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            subscriptions = self.model.objects.filter(user=self.request.user)
            return UserPost.objects.filter(
                user__in=[
                    subscribe.author_blog.pk for subscribe in subscriptions
                ]
            )


class ReadPostView(View):
    model = ReadPost
    success_url = reverse_lazy('news-feed')

    def post(self, request, *args, **kwargs):
        post_pk = request.POST.get('read', '')
        if post_pk:
            try:
                ReadPost.objects.get(
                    user_id=request.user, post_id=post_pk).delete()
            except ReadPost.DoesNotExist as e:
                ReadPost.objects.create(
                    user_id=request.user.pk, post_id=post_pk)
        return HttpResponseRedirect(LOGIN_REDIRECT_URL)


class CreatePost(CreateView):
    template_name = 'personalblogapp/create_post.html'
    model = UserPost
    fields = ['title', 'text']
    success_url = reverse_lazy('user-posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'создание поста'
        return context

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()
        return super().form_valid(form)


class UserPosts(ListView):
    template_name = 'personalblogapp/user_posts.html'
    model = UserPost
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'мои посты'
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return UserPost.objects.filter(user=self.request.user)
