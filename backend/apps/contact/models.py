from django.db import models


class ContactMessage(models.Model):
    nom          = models.CharField(max_length=150)
    email        = models.EmailField()
    message      = models.TextField()
    date_message = models.DateTimeField(auto_now_add=True)
    lu           = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date_message"]

    def __str__(self):
        return f"{self.nom} — {self.email}"
