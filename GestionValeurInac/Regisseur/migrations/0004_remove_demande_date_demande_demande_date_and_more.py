# Generated by Django 5.0.7 on 2024-08-01 13:45

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regisseur', '0003_remove_demande_quantite_remove_demande_type_valeur_and_more'),
        ('Stock', '0007_alter_mouvementstock_date_mouvement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='date_demande',
        ),
        migrations.AddField(
            model_name='demande',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='demande',
            name='valeur_inactive',
            field=models.ForeignKey(default=0.0005928853754940711, on_delete=django.db.models.deletion.CASCADE, to='Stock.valeurinactive'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DemandeValeur',
        ),
    ]
