# Generated by Django 4.0 on 2021-12-30 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_personality_villager_catchphrase_villager_fav_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personality',
            options={'verbose_name_plural': 'personalities'},
        ),
    ]
