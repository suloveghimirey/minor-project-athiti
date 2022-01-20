# Generated by Django 3.2.9 on 2022-01-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_alter_booking_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_email',
            field=models.EmailField(default='Add', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='idx',
            field=models.CharField(default='a', max_length=100),
        ),
    ]
