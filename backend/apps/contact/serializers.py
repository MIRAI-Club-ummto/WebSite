from rest_framework import serializers
from .models import ContactMessage


class ContactMessagePublicSerializer(serializers.ModelSerializer):
    """Soumission publique : uniquement les champs du formulaire."""

    class Meta:
        model = ContactMessage
        fields = ["id", "nom", "email", "message", "date_message"]
        read_only_fields = ["id", "date_message"]


class ContactMessageAdminSerializer(serializers.ModelSerializer):
    """Vue admin : inclut le statut lu/non-lu."""

    class Meta:
        model = ContactMessage
        fields = ["id", "nom", "email", "message", "date_message", "lu"]
        read_only_fields = ["id", "date_message"]
