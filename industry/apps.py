"""App Configuration"""

# Django
from django.apps import AppConfig

# AA Example App
from industry import __version__


class IndustryConfig(AppConfig):
    """App Config"""

    default_auto_field = "django.db.models.AutoField"
    author = "Geuthur"
    name = "industry"
    label = "industry"
    verbose_name = f"Industry v{__version__}"
