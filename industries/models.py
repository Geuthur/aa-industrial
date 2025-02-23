"""Models for Industries."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from esi.models import Token

from industries.managers import IndustriesManager


class General(models.Model):
    """General model for app permissions"""

    class Meta:
        abstract = True  # Please Remove this to activate this model
        managed = False
        permissions = (("basic_access", _("Can access this app")),)
        default_permissions = ()


class Industries(models.Model):
    """Industries model for app"""

    token = models.ForeignKey(
        Token,
        on_delete=models.CASCADE,
        related_name="industries",
        verbose_name=_("Token"),
    )

    class Meta:
        abstract = True  # Please Remove this to activate this model
        managed = False
        verbose_name = _("Industries")
        verbose_name_plural = _("Industriess")

    def __str__(self):
        return f"{self.token.character_name} - {self.token.character_id}"

    objects = IndustriesManager()
