from django.apps import AppConfig


class CsvApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "csv_api"

    def ready(self):
        import csv_api.signals
