from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display  = ["titre", "date_evenement", "lieu"]
    search_fields = ["titre", "description_courte", "lieu"]
    ordering      = ["date_evenement"]
