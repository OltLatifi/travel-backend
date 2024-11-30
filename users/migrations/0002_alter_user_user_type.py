# Generated by Django 4.2 on 2024-11-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("Traveler", "Traveler"),
                    ("Host", "Host"),
                    ("Staff", "Staff"),
                ],
                max_length=10,
            ),
        ),
    ]
