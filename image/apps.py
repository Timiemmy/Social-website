from django.apps import AppConfig


class ImageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "image"

    def ready(self):
        # This will be imported through the ready method when the images app is loaded
        import image.signals
