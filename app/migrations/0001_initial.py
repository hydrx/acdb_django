# Generated by Django 4.0 on 2021-12-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='villagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('species', models.CharField(max_length=12)),
                ('birthday_month', models.IntegerField()),
                ('birthday_day', models.IntegerField()),
            ],
        ),
    ]
