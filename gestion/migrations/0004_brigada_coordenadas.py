# Generated by Django 5.2 on 2025-05-07 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_brigada_miembros'),
    ]

    operations = [
        migrations.AddField(
            model_name='brigada',
            name='coordenadas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestion.coordenada'),
        ),
    ]
