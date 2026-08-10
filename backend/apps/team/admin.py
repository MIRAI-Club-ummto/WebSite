from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display  = ["prenom", "nom", "poste", "ordre_affichage"]
    search_fields = ["prenom", "nom", "poste"]
    ordering      = ["ordre_affichage"]
    list_editable = ["ordre_affichage"]
