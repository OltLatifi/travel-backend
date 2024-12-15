from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Airport, Flight, Ticket, Airline
from .serializers import AirportSerializer, FlightSerializer, TicketSerializer, AirlineSerializer
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

class FlightListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsStaffUser]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

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
    queryset = Flight.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10

    result_page = paginator.paginate_queryset(queryset, request)

    serializer = FlightSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
