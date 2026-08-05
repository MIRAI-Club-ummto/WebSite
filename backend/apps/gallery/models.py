from django.db import models


class GalleryItem(models.Model):
    TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Vidéo"),
    ]

    evenement   = models.PositiveIntegerField(null=True, blank=True, help_text="ID de l'événement associé (optionnel)")
    type        = models.CharField(max_length=10, choices=TYPE_CHOICES, default="image")
    description = models.CharField(max_length=255, blank=True)
    image_url   = models.URLField(max_length=500, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.description or f"Média #{self.pk}"
