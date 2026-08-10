from rest_framework import serializers
from .models import WebsiteSettings


class WebsiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteSettings
        fields = ["logo_url", "slogan", "description", "photo_couverture_url",
                  "email", "instagram", "facebook", "linkedin", "github", "updated_at"]
        read_only_fields = ["updated_at"]
