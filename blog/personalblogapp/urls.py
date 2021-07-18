from django.contrib.auth.views import LoginView
from django.urls import path

from .views import NewsFeed

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('', NewsFeed.as_view(), name='news-feed'),
]
