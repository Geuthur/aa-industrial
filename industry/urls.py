"""App URLs"""

from django.urls import path

from industry import views

app_name: str = "industry"

urlpatterns = [
    path("", views.index, name="index"),
]
