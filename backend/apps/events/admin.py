from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("titre", "date", "heure", "lieu")
    search_fields = ("titre", "lieu")
    list_filter = ("date",)