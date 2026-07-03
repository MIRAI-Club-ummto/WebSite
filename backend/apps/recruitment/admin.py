from django.contrib import admin
from .models import Candidature, RecruitmentSettings


@admin.register(RecruitmentSettings)
class RecruitmentSettingsAdmin(admin.ModelAdmin):
    list_display = ["recrutements_ouverts", "date_ouverture_candidatures", "date_limite_candidatures"]

    def has_add_permission(self, request):
        return not RecruitmentSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Candidature)
class CandidatureAdmin(admin.ModelAdmin):
    list_display  = ["prenom", "nom", "email", "niveau_etude", "statut", "date_candidature"]
    list_filter   = ["statut", "niveau_etude"]
    search_fields = ["prenom", "nom", "email"]
    list_editable = ["statut"]
