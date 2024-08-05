from django.contrib import admin


from .models import Regisseur,DemandeValeur,Demande


class DemandeValeurAdmin(admin.ModelAdmin):
    list_display = ["demande", "valeur_inactive", "quantite"]


class DemandeAdmin(admin.ModelAdmin):
    change_form_template = "change_form.html"


admin.site.register(Regisseur)
admin.site.register(DemandeValeur, DemandeValeurAdmin)
admin.site.register(Demande,DemandeAdmin)
