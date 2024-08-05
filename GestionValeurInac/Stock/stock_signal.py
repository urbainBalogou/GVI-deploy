from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MouvementStock, ValeurInactive, Stockage

@receiver(post_save, sender=MouvementStock)
def update_valeur_inactive(sender, instance, **kwargs):
    valeur_inactive = instance.valeur_inactive
    if instance.type_mouvement == 'ENTREE':
        valeur_inactive.nombre_de_feuillets += instance.quantite
    elif instance.type_mouvement == 'SORTIE':
        valeur_inactive.nombre_de_feuillets -= instance.quantite
    valeur_inactive.save()

    # Update stockage
    stockage, created = Stockage.objects.get_or_create(
        commune=instance.regisseur.commune,
        type_valeur=instance.valeur_inactive.type_valeur
    )
    if instance.type_mouvement == 'ENTREE':
        stockage.quantiteDispo += instance.quantite
    elif instance.type_mouvement == 'SORTIE':
        stockage.quantiteDispo -= instance.quantite
    stockage.Montant = stockage.quantiteDispo * instance.valeur_inactive.type_valeur.valeur_faciale
    stockage.save()
