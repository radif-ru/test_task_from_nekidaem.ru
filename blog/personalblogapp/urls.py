from django.contrib.auth.views import LoginView
from django.urls import path

from .views import NewsFeed, ReadPosts, CreatePost, UserPosts, SubscribeBlog

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('', NewsFeed.as_view(), name='news-feed'),
    path('read/', ReadPosts.as_view(), name='read-post'),
    path('create/', CreatePost.as_view(), name='create-post'),
    path('myposts/', UserPosts.as_view(), name='user-posts'),
    path('subscribe/', SubscribeBlog.as_view(), name='subscribe-blog'),
]
