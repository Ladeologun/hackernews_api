from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        print("starting scheduler............")
        from .item_scheduler import item_updater
        item_updater.start()

