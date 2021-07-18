from django.contrib.auth.views import LoginView
from django.urls import path

from .views import UserHome

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('', UserHome.as_view(), name='user-home'),
]
