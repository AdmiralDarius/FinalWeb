# Generated by Django 2.1.4 on 2019-01-27 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_player_team'),
        ('games', '0007_game_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='first_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_player', to='info.Player'),
        ),
        migrations.AddField(
            model_name='event',
            name='second_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_player', to='info.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='best_player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Player'),
        ),
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='games.Game'),
        ),
    ]
