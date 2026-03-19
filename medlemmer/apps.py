from django.apps import AppConfig


class MedlemmerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medlemmer'

    def ready(self):
        import medlemmer.signals
