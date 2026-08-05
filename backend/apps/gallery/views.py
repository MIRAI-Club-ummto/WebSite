from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import GalleryItem
from .serializers import GalleryItemSerializer


class GalleryItemViewSet(viewsets.ModelViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["evenement", "type"]
    search_fields    = ["description"]
    ordering         = ["-created_at"]
