# payments/models.py
from django.db import models
from properties.models import Booking
from vehicles.models import VehicleBooking
from users.models import User

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer'),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    vehicle_booking = models.ForeignKey(VehicleBooking, on_delete=models.CASCADE, null=True, blank=True)
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
