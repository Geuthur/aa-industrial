"""App Tasks"""

from celery import shared_task

from industry.hooks import get_extension_logger

logger = get_extension_logger(__name__)


@shared_task
def update_all_industry():
    """Update all industry."""
    # pylint: disable=unnecessary-pass
    pass
