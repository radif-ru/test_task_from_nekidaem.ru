from django.contrib import admin

from personalblogapp.models import UserPost, ReadPost, UserSubscribeBlog

admin.site.register(UserPost)
admin.site.register(ReadPost)
admin.site.register(UserSubscribeBlog)
