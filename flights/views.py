from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Airport, Flight
from .serializers import AirportSerializer, FlightSerializer
from users.permissions import IsStaffUser

class AirportListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class AirportDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class FlightListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer