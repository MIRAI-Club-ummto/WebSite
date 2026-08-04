from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import ContactMessage
from .serializers import ContactMessagePublicSerializer, ContactMessageAdminSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    """
    POST   /api/contact/messages/          -> envoyer un message (public)
    GET    /api/contact/messages/          -> liste (admin)
    GET    /api/contact/messages/{id}/     -> détail (admin)
    PATCH  /api/contact/messages/{id}/     -> marquer comme lu (admin)
    DELETE /api/contact/messages/{id}/     -> supprimer (admin)
    """

    filter_backends  = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["lu"]
    search_fields    = ["nom", "email", "message"]
    ordering         = ["-date_message"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ContactMessage.objects.all()
        return ContactMessage.objects.none()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return ContactMessageAdminSerializer
        return ContactMessagePublicSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        serializer = ContactMessagePublicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["patch"], url_path="marquer-lu")
    def marquer_lu(self, request, pk=None):
        message = self.get_object()
        message.lu = True
        message.save()
        serializer = ContactMessageAdminSerializer(message)
        return Response(serializer.data)
