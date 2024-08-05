from django import forms
from .models import MouvementStock, ValeurInactive,Stockage
from Commune.models import Commune


class ValeurInactiveAdminForm(forms.ModelForm):
    class Meta:
        model = ValeurInactive
        fields = ['type_valeur', 'nombre_de_valeur_feuillet_ou_carnet', 'nombre_de_feuillets', 'montant_total', 'date_enreg']
        widgets = {
            'montant_total': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'date_enreg': forms.DateInput(attrs={'readonly': 'readonly'}),
        }


class StockAdminForm(forms.ModelForm):
    class Meta:
        model = Stockage
        fields = ['commune', 'type_valeur', 'quantiteDispo', 'Montant']
        widgets = {


            'quantiteDispo': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'Montant': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }



class MouvementStockForm(forms.ModelForm):
    class Meta:
        model = MouvementStock
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        type_mouvement = cleaned_data.get("type_mouvement")
        quantite = cleaned_data.get("quantite")
        regisseur = cleaned_data.get("regisseur")  # Assurez-vous que ce champ existe
        type_valeur = cleaned_data.get("type_valeur")

        if type_mouvement == 'sortie':
            commune = regisseur.commune
            stock_disponible = regisseur.get_stock_disponible(type_valeur)
            if quantite > stock_disponible:
                self.add_error("quantite", f"La quantité demandée ({quantite}) dépasse la quantité disponible ({stock_disponible}) pour la commune {commune.nom} et le type de valeur {type_valeur.nom}. Veuillez entrer une quantité valide.")

        return cleaned_data
