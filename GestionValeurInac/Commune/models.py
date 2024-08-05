from django.db import models


class Commune(models.Model):
    code_commune = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=255)
    mail = models.EmailField(null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


