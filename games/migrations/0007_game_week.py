# Generated by Django 2.1.4 on 2019-01-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_league_is_football'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='week',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]