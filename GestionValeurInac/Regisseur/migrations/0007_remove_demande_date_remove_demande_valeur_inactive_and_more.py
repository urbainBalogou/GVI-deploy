# Generated by Django 5.0.7 on 2024-08-01 14:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Regisseur', '0006_demande'),
        ('Stock', '0007_alter_mouvementstock_date_mouvement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='date',
        ),
        migrations.RemoveField(
            model_name='demande',
            name='valeur_inactive',
        ),
        migrations.AddField(
            model_name='demande',
            name='date_demande',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DemandeValeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('demande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demande_valeurs', to='Regisseur.demande')),
                ('valeur_inactive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stock.valeurinactive')),
            ],
        ),
    ]
