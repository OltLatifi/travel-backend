# payments/models.py
from django.db import models
from flights.models import Flight
from properties.models import Booking, Property
from users.models import User

class BookingReservation(models.Model):
    customer_name = models.CharField(max_length=255, default="John Doe")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_reservations", null=True, blank=True)
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    nights = models.PositiveBigIntegerField(default=1)
    amount = models.PositiveBigIntegerField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('Credit Card', 'Credit Card'),
    ]
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True)
    traveler = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.PositiveBigIntegerField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
