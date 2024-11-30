from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from vehicles.serializers import VehicleBookingSerializer
from .models import Vehicle, VehicleBooking
from .serializers import VehicleSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VehicleBookingListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer

class VehicleBookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VehicleBooking.objects.all()
    serializer_class = VehicleBookingSerializer
