from django.contrib.auth.views import LoginView
from django.urls import path

from .views import NewsFeed, ReadPostView, CreatePost

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('', NewsFeed.as_view(), name='news-feed'),
    path('read/', ReadPostView.as_view(), name='read-post'),
    path('create/', CreatePost.as_view(), name='create-post')
]
