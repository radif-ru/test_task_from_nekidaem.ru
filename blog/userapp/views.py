from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class UserHome(ListView):
    template_name = 'userapp/index.html'
    model = User
    context_object_name = 'user'
