from rest_framework import serializers
from .models import Vehicle, VehicleBooking

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id', 'host', 'make', 'model', 'year', 'vehicle_type',
            'price_per_day', 'location', 'availability_status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class VehicleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBooking
        fields = [
            'id', 'vehicle', 'traveler', 'rental_start_date', 'rental_end_date',
            'total_price', 'booking_status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
