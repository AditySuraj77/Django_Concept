# Generated by Django 4.2.1 on 2023-06-14 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_player_name_alter_player_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='slug',
        ),
    ]
