from django.utils import timezone
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    est_passe = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "titre", "description_courte", "description_complete",
                  "date_evenement", "lieu", "icon", "image_url",
                  "programme", "intervenants", "liens_utiles",
                  "est_passe", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at", "est_passe"]

    def get_est_passe(self, obj):
        return obj.date_evenement < timezone.now()
