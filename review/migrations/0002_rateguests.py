# Generated by Django 3.2.9 on 2022-01-08 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateGuests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=500)),
                ('rating', models.FloatField()),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Guest', to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Host', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]