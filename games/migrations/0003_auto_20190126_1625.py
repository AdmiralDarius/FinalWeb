# Generated by Django 2.1.4 on 2019-01-26 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20190126_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='basketball_states',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.BasketbalState'),
        ),
        migrations.AlterField(
            model_name='game',
            name='football_states',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games.FootballState'),
        ),
        migrations.AlterField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1_reverse', to='info.Team'),
        ),
        migrations.AlterField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2_reverse', to='info.Team'),
        ),
    ]