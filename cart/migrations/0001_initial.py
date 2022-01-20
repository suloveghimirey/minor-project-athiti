# Generated by Django 3.2.9 on 2021-12-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
