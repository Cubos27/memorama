# Generated by Django 5.0.3 on 2024-03-25 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_subpartidas_numerojugadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subpartidas',
            name='cartaID',
        ),
        migrations.AddField(
            model_name='cartas',
            name='partidaID',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='game.partidas'),
        ),
        migrations.AddField(
            model_name='subpartidas',
            name='cartasEnPartidaID',
            field=models.ManyToManyField(to='game.cartasenpartida'),
        ),
        migrations.AlterField(
            model_name='subpartidas',
            name='numeroJugadores',
            field=models.IntegerField(),
        ),
    ]
