# Generated by Django 5.0.3 on 2024-03-25 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0011_remove_subpartidas_cartaid_cartas_partidaid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartas',
            name='partidaID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.partidas'),
        ),
    ]
