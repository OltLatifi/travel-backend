# vehicles/models.py
from django.db import models
from users.models import User

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('Car', 'Car'),
        ('Van', 'Van'),
        ('Bike', 'Bike'),
        ('Scooter', 'Scooter'),
        ('Other', 'Other'),
    ]
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehicles")
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VehicleBooking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vehicle_bookings")
    rental_start_date = models.DateField()
    rental_end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
