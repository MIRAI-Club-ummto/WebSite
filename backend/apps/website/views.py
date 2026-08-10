from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import WebsiteSettings
from .serializers import WebsiteSettingsSerializer


class WebsiteSettingsView(APIView):
    """
    GET /api/website/settings/  -> paramètres publics du site
    PUT /api/website/settings/  -> mise à jour (admin uniquement)
    """

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        settings = WebsiteSettings.get()
        return Response(WebsiteSettingsSerializer(settings).data)

    def put(self, request):
        settings = WebsiteSettings.get()
        serializer = WebsiteSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
