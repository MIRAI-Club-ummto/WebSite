from django.utils import timezone
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields    = ["titre", "description_courte", "lieu"]
    ordering_fields  = ["date_evenement", "titre"]
    ordering         = ["date_evenement"]

    @action(detail=False, methods=["get"], url_path="upcoming")
    def upcoming(self, request):
        events = Event.objects.filter(date_evenement__gte=timezone.now()).order_by("date_evenement")
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="past")
    def past(self, request):
        events = Event.objects.filter(date_evenement__lt=timezone.now()).order_by("-date_evenement")
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
