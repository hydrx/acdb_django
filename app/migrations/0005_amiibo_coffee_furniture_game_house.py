# Generated by Django 4.0 on 2021-12-31 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_personality_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amiibo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=20, unique=True)),
                ('card_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beans', models.CharField(max_length=20)),
                ('milk', models.CharField(max_length=8)),
                ('sugar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('style', models.CharField(blank=True, max_length=20)),
                ('on_surface', models.BooleanField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('console', models.CharField(max_length=12)),
                ('year_released', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallpaper', models.CharField(max_length=16)),
                ('floor', models.CharField(max_length=16)),
                ('music', models.CharField(blank=True, max_length=16)),
            ],
        ),
    ]
