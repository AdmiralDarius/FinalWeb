# Generated by Django 2.1.4 on 2019-02-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_playersgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersgame',
            name='bench',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
