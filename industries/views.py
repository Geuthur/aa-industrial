"""PvE Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from .hooks import get_extension_logger

logger = get_extension_logger(__name__)


@login_required
@permission_required("industries.basic_access")
def index(request):
    context = {}
    return render(request, "industries/index.html", context=context)


@login_required
@permission_required("industries.basic_access")
def industry(request):
    context = {}
    return render(request, "industries/test_view.html", context=context)
