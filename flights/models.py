from django.db import models
from users.models import User


class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Flight(models.Model):
    airline_name = models.CharField(max_length=255)
    flight_number = models.CharField(max_length=50)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departing_flights")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arriving_flights")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tickets")
    seat_number = models.CharField(max_length=10, blank=True, null=True)
    booking_status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

