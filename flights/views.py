from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Airport, Flight, Ticket
from .serializers import AirportSerializer, FlightSerializer, TicketSerializer
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

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]