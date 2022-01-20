# Generated by Django 3.2.9 on 2022-01-05 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0035_auto_20220105_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room_host_fullname',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_host_full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_host_id',
            field=models.IntegerField(),
        ),
    ]
