# Generated by Django 3.2.9 on 2022-01-29 09:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0050_alter_listing_kitchen_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]