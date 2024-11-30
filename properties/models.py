# properties/models.py
from django.db import models
from users.models import User

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Hotel', 'Hotel'),
        ('Hostel', 'Hostel'),
        ('Other', 'Other'),
    ]
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    max_guests = models.PositiveIntegerField()
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=10, choices=BOOKING_STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Include other models like Image, Review, Feature, and FeatureMapping here as needed.