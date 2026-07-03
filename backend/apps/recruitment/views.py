from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Candidature, RecruitmentSettings
from .serializers import (
    CandidaturePublicSerializer,
    CandidatureAdminSerializer,
    RecruitmentSettingsSerializer,
)


class RecruitmentSettingsView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        settings = RecruitmentSettings.get()
        return Response(RecruitmentSettingsSerializer(settings).data)

    def put(self, request):
        settings = RecruitmentSettings.get()
        serializer = RecruitmentSettingsSerializer(settings, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CandidatureViewSet(viewsets.ModelViewSet):
    filter_backends  = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["statut", "niveau_etude"]
    search_fields    = ["prenom", "nom", "email", "departement"]
    ordering         = ["-date_candidature"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Candidature.objects.all()
        return Candidature.objects.none()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return CandidatureAdminSerializer
        return CandidaturePublicSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        settings = RecruitmentSettings.get()
        phase = RecruitmentSettingsSerializer(settings).data["phase"]
        if phase != "ouvert":
            msg = {
                "ferme":       "Les candidatures sont actuellement fermées.",
                "non_demarre": "Les candidatures ne sont pas encore ouvertes.",
            }
            return Response({"detail": msg.get(phase, "Indisponible.")}, status=status.HTTP_403_FORBIDDEN)

        serializer = CandidaturePublicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["patch"], url_path="statut")
    def update_statut(self, request, pk=None):
        candidature = self.get_object()
        serializer = CandidatureAdminSerializer(candidature, data={"statut": request.data.get("statut")}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
