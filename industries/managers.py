# Django
from django.db import models

# AA Voices of War
from industries.hooks import get_extension_logger

logger = get_extension_logger(__name__)


class IndustriesQuerySet(models.QuerySet):
    pass


class IndustriesManagerBase(models.Manager):
    pass


IndustriesManager = IndustriesManagerBase.from_queryset(IndustriesQuerySet)
