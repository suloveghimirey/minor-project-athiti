# Generated by Django 3.2.9 on 2021-12-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_rename_bookings_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
    ]
