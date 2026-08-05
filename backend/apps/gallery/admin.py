from django.contrib import admin
from .models import GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display  = ["description", "type", "evenement", "created_at"]
    list_filter   = ["type"]
    search_fields = ["description"]
    ordering      = ["-created_at"]
