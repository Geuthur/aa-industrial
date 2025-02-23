"""App Configuration"""

# Django
from django.apps import AppConfig

# AA Example App
from industries import __version__


class IndustriesConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.AutoField"
    author = "Geuthur"
    name = "industries"
    label = "industries"
    verbose_name = f"Industries v{__version__}"
