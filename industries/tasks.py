"""App Tasks"""

from celery import shared_task

from industries.hooks import get_extension_logger

logger = get_extension_logger(__name__)


@shared_task
def update_all_industries():
    """Update all industries."""
    # pylint: disable=unnecessary-pass
    pass
