from django.db import models


class Event(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()

    date = models.DateField()
    heure = models.TimeField()

    lieu = models.CharField(max_length=255)

    photo = models.ImageField(blank=True, null=True)
    lien = models.URLField(blank=True)

    def __str__(self):
        return self.titre