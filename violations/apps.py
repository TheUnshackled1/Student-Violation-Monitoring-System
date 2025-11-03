from django.apps import AppConfig


class ViolationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "violations"
    def ready(self):  # noqa: D401
        """Import signals for model hooks."""
        try:
            from . import signals  # noqa: F401
        except Exception:
            # Avoid breaking on migration commands before app is fully loaded
            pass
