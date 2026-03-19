from django.apps import AppConfig


class KontingentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kontingent'

    def ready(self):
        import kontingent.signals
