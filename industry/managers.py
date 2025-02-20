# Django
from django.db import models

# AA Voices of War
from industry.hooks import get_extension_logger

logger = get_extension_logger(__name__)


class IndustryQuerySet(models.QuerySet):
    pass


class IndustryManagerBase(models.Manager):
    pass


IndustryManager = IndustryManagerBase.from_queryset(IndustryQuerySet)
