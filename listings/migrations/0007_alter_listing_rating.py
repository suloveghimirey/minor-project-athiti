# Generated by Django 3.2.9 on 2021-12-01 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
