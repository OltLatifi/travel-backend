from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Airport, Flight, Ticket, Airline
from .serializers import AirportSerializer, FlightSerializer, FlightSerializerPresentation, TicketSerializer, AirlineSerializer
from users.permissions import IsStaffUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination

class AirportListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class AirportDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class FlightListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Flight.objects.filter(departure_time__gte=datetime.now(timezone.utc)).order_by('departure_time')
    serializer_class = FlightSerializerPresentation

class FlightCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Flight.objects.filter(departure_time__gte=datetime.now(timezone.utc))
    serializer_class = FlightSerializer

class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializerPresentation

class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, IsStaffUser]

class AirlineListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AirlineDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_flights(request):
    queryset = Flight.objects.all().prefetch_related('airline', 'departure_airport', 'arrival_airport')

    serializer = FlightSerializerPresentation(queryset, many=True)
    return Response(serializer.data)
