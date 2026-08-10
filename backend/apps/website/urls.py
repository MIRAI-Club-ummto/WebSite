from django.urls import path
from .views import WebsiteSettingsView

urlpatterns = [
    path("settings/", WebsiteSettingsView.as_view(), name="website-settings"),
]
