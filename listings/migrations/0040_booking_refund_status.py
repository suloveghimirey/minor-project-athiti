# Generated by Django 3.2.9 on 2022-01-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0039_alter_booking_date_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='refund_status',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
