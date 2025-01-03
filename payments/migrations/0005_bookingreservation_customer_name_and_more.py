# Generated by Django 5.1.4 on 2024-12-17 20:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_remove_payment_vehicle_booking_payment_flight_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreservation',
            name='customer_name',
            field=models.CharField(default='John Doe', max_length=255),
        ),
        migrations.AddField(
            model_name='bookingreservation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]
