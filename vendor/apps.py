from django.apps import AppConfig


class VendorSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor'

    def ready(self):
        import vendor.signals
