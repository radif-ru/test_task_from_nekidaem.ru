from django.apps import AppConfig


class PersonalBlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personal_blog'

    def ready(self):
        import personal_blog.signals.handlers  # handlers
