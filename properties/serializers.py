from rest_framework import serializers
from .models import Property, Booking, Image, Review

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id', 'host', 'name', 'description', 'location', 'latitude',
            'longitude', 'price_per_night', 'max_guests', 'property_type',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'property', 'traveler', 'check_in_date', 'check_out_date',
            'total_price', 'booking_status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'property', 'image_url', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'traveler', 'property', 'rating', 'review_text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
