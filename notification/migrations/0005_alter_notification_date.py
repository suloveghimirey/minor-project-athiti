# Generated by Django 3.2.9 on 2022-01-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_alter_notification_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
