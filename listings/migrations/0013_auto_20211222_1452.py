# Generated by Django 3.2.9 on 2021-12-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_auto_20211221_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]
