# Generated by Django 5.0.7 on 2024-07-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_commune', models.CharField(max_length=100, unique=True)),
                ('nom', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=254)),
                ('adresse', models.TextField()),
            ],
        ),
    ]
