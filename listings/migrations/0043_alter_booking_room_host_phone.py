# Generated by Django 3.2.9 on 2022-01-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0042_auto_20220108_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='room_host_phone',
            field=models.IntegerField(),
        ),
    ]
