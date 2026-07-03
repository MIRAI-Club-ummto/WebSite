from rest_framework import serializers
from .models import Resource


class ResourceSerializer(serializers.ModelSerializer):
    categorie_label = serializers.SerializerMethodField()

    class Meta:
        model = Resource
        fields = ["id", "titre", "description", "categorie", "categorie_label",
                  "fichier_url", "evenement", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at", "categorie_label"]

    def get_categorie_label(self, obj):
        return obj.get_categorie_display()
