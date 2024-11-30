from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Property, Booking, Image, Review
from .serializers import PropertySerializer, BookingSerializer, ImageSerializer, ReviewSerializer

class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

class ImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
