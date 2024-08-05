from django.db import models
from Regisseur.models import Regisseur
from Commune.models import Commune
from datetime import date

class TypeValeurInactive(models.Model):
    nature = models.CharField(max_length=255)
    valeur_faciale = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nature}-{self.valeur_faciale}"

class ValeurInactive(models.Model):
    type_valeur = models.ForeignKey(TypeValeurInactive, on_delete=models.CASCADE)
    nombre_de_valeur_feuillet_ou_carnet = models.PositiveIntegerField()
    nombre_de_feuillets = models.PositiveIntegerField()
    montant_total = models.IntegerField(default=0)
    date_enreg = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.type_valeur.nature} - {self.nombre_de_feuillets} feuillets"

class MouvementStock(models.Model):
    valeur_inactive = models.ForeignKey(ValeurInactive, on_delete=models.CASCADE)
    regisseur = models.ForeignKey(Regisseur, on_delete=models.CASCADE)
    type_mouvement = models.CharField(max_length=10, choices=[('ENTREE', 'Entrée'), ('SORTIE', 'Sortie')])
    quantite = models.PositiveIntegerField()
    date_mouvement = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.type_mouvement} - {self.valeur_inactive} par {self.regisseur.nom}"

class Stockage(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    type_valeur = models.ForeignKey(TypeValeurInactive, on_delete=models.CASCADE)
    quantiteDispo = models.PositiveIntegerField(default=0)
    Montant = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.commune} dispose {self.quantiteDispo} quantités de {self.type_valeur}"




