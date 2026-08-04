from django.db import models


class Event(models.Model):
    titre                = models.CharField(max_length=255)
    description_courte   = models.CharField(max_length=500, blank=True)
    description_complete = models.TextField(blank=True)
    date_evenement       = models.DateTimeField()
    lieu                 = models.CharField(max_length=255, blank=True)
    icon                 = models.CharField(max_length=10, blank=True, default="📅")
    image_url            = models.URLField(max_length=500, blank=True)

    programme     = models.JSONField(default=list, blank=True)
    intervenants  = models.JSONField(default=list, blank=True)
    liens_utiles  = models.JSONField(default=list, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["date_evenement"]

    def __str__(self):
        return self.titre
