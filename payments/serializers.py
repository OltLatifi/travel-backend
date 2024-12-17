from rest_framework import serializers
from .models import BookingReservation

from properties.serializers import PropertySerializer

class BookingReservationSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    class Meta:
        model = BookingReservation
        fields = ['id', 'customer_name', 'user', 'property', 'nights', 'amount', 'completed', 'created_at']
