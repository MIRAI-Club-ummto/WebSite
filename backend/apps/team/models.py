from django.db import models


class Member(models.Model):
    prenom          = models.CharField(max_length=100)
    nom             = models.CharField(max_length=100)
    poste           = models.CharField(max_length=150)
    description     = models.TextField(blank=True)
    linkedin        = models.URLField(max_length=500, blank=True)
    github          = models.URLField(max_length=500, blank=True)
    photo_url       = models.URLField(max_length=500, blank=True)
    ordre_affichage = models.PositiveIntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["ordre_affichage"]

    def __str__(self):
        return f"{self.prenom} {self.nom} — {self.poste}"
