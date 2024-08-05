from django.db import models
from Commune.models import Commune


class Regisseur(models.Model):
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    mail = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    def get_stock_disponible(self, type_valeur):
        from Stock.models import Stockage
        stock = Stockage.objects.filter(commune=self.commune, type_valeur=type_valeur).first()
        if stock:
            return stock.quantiteDispo
        return 0


from Stock.models import TypeValeurInactive, ValeurInactive


class Demande(models.Model):
    regisseur = models.ForeignKey(Regisseur, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Demande #{self.id} par {self.regisseur.nom} {self.regisseur.prenom} le {self.date_demande}"


class DemandeValeur(models.Model):
    demande = models.ForeignKey(Demande, on_delete=models.CASCADE, related_name='demande_valeurs')
    valeur_inactive = models.ForeignKey(ValeurInactive, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} de {self.valeur_inactive.type_valeur.nature} pour la demande {self.demande.id}"

