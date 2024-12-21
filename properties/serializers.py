from rest_framework import serializers
from .models import Property, Booking, Image, Review

class PropertySerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            'id', 'host', 'name', 'description', 'location', 'latitude',
            'longitude', 'price_per_night', 'max_guests', 'property_type',
            'created_at', 'updated_at', 'available', 'images'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'host', 'images']

    def create(self, validated_data):
        validated_data['host'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_images(self, obj):
        images = Image.objects.filter(property=obj)
        return [image.image.url for image in images]

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
