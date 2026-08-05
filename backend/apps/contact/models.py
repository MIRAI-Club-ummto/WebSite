from django.db import models
class contact(models.Model):

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom