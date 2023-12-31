# Generated by Django 4.2.1 on 2023-06-14 10:23

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_player_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from=models.TextField(), unique=True),
        ),
    ]
