# Generated by Django 3.2.9 on 2021-12-21 10:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0010_bookings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bookings',
            new_name='Booking',
        ),
    ]
