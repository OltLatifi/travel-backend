# Generated by Django 4.2 on 2024-11-30 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Airport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Flight",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("airline_name", models.CharField(max_length=255)),
                ("flight_number", models.CharField(max_length=50)),
                ("departure_time", models.DateTimeField()),
                ("arrival_time", models.DateTimeField()),
                ("duration_minutes", models.PositiveIntegerField()),
                (
                    "price_per_ticket",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "arrival_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="arriving_flights",
                        to="flights.airport",
                    ),
                ),
                (
                    "departure_airport",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departing_flights",
                        to="flights.airport",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seat_number", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "booking_status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Confirmed", "Confirmed"),
                            ("Cancelled", "Cancelled"),
                        ],
                        default="Pending",
                        max_length=10,
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "flight",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="flights.flight",
                    ),
                ),
                (
                    "traveler",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
