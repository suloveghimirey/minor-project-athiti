# Generated by Django 3.2.9 on 2021-11-30 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='room_type',
            field=models.CharField(choices=[('Air Conditioner', 'Ac'), ('No Air Conditioner', 'No Ac')], default='Air Conditioner', max_length=30),
        ),
    ]