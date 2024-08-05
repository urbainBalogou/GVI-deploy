from django.db import IntegrityError, transaction

from .models import MouvementStock, TypeValeurInactive, Stockage
from django.contrib import admin, messages
from .models import ValeurInactive
from .admin_forms import ValeurInactiveAdminForm, StockAdminForm


class ValeurInactiveAdmin(admin.ModelAdmin):
    form = ValeurInactiveAdminForm

    class Media:
        js = ('js/admin_valeur_inactive.js',)


class StockageAdmin(admin.ModelAdmin):
    form = StockAdminForm

    class Media:
        js = ('js/admin_valeur_inactive.js',)


class MouvementStockAdmin(admin.ModelAdmin):


    @transaction.atomic
    def save_model(self, request, obj, form, change):
        try:
            obj.save()
            messages.success(request, "Le mouvement de stock a été enregistré avec succès.")
        except IntegrityError:
            messages.error(request, "La quantité demandée dépasse la quantité disponible.")





admin.site.register(ValeurInactive, ValeurInactiveAdmin)
admin.site.register(MouvementStock, MouvementStockAdmin)
admin.site.register(TypeValeurInactive)
admin.site.register(Stockage,StockageAdmin)
