from rest_framework import serializers
from .models import Airport, Flight, Ticket, Airline

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['id', 'name', 'IATA_code']
        

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'code', 'name', 'city', 'country']


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id', 'airline', 'flight_number', 'departure_airport', 
            'arrival_airport', 'departure_time', 'arrival_time', 
            'duration_minutes', 'price_per_ticket', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id', 'flight', 'traveler', 'seat_number', 'booking_status',
            'price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
