from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidatureViewSet, RecruitmentSettingsView

router = DefaultRouter()
router.register(r"candidatures", CandidatureViewSet, basename="candidature")

urlpatterns = [
    path("settings/", RecruitmentSettingsView.as_view(), name="recruitment-settings"),
    path("", include(router.urls)),
]
