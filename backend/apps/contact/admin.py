from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display  = ["nom", "email", "lu", "date_message"]
    list_filter   = ["lu"]
    search_fields = ["nom", "email", "message"]
    ordering      = ["-date_message"]
    list_editable = ["lu"]
