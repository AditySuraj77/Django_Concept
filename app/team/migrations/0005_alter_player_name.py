# Generated by Django 4.2.1 on 2023-06-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_remove_player_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
