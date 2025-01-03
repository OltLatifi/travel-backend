# Generated by Django 5.1.4 on 2024-12-17 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_bookingreservation_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreservation',
            name='amount',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookingreservation',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
