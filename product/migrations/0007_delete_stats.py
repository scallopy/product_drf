# Generated by Django 4.1 on 2022-09-12 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_stats_end_date_alter_stats_start_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Stats',
        ),
    ]
