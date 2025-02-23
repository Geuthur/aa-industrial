"""App URLs"""

from django.urls import path

from industries import views

app_name: str = "industries"

urlpatterns = [
    path("", views.index, name="index"),
]
