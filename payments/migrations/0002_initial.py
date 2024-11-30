# Generated by Django 5.0.3 on 2024-11-30 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("payments", "0001_initial"),
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="booking",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="properties.booking",
            ),
        ),
    ]
