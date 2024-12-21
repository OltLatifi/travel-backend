from rest_framework import serializers

from flights.serializers import FlightSerializer
from .models import BookingReservation, FlightReservation

from properties.serializers import PropertySerializer

class BookingReservationSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    class Meta:
        model = BookingReservation
        fields = ['id', 'customer_name', 'user', 'property', 'nights', 'amount', 'completed', 'created_at']

class FlightReservationSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    class Meta:
        model = FlightReservation
        fields = ['id', 'customer_name', 'user', 'flight', 'seats', 'amount', 'completed', 'created_at']