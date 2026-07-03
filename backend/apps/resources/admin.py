from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display  = ["titre", "categorie", "evenement", "created_at"]
    list_filter   = ["categorie"]
    search_fields = ["titre", "description"]
