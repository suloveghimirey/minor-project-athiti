# Generated by Django 3.2.9 on 2022-01-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_auto_20220105_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_host_email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user_email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
