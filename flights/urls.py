from django.urls import path
from .views import AirportListCreateView, AirportDetailView, FlightDetailView, FlightListCreateView, TicketDetailView, TicketListCreateView, AirlineListCreateView, AirlineDetailView

urlpatterns = [
    path("airport/", AirportListCreateView.as_view(), name="airport-list-create"),
    path("airport/<int:pk>/", AirportDetailView.as_view(), name="airport-detail"),
    
    path('', FlightListCreateView.as_view(), name='flight-list-create'),
    path('<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),

    path('tickets/', TicketListCreateView.as_view(), name='ticket-list-create'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),

    path('airlines/', AirlineListCreateView.as_view(), name='airline-list-create'),
    path('airlines/<int:pk>/', AirlineDetailView.as_view(), name='airline-detail'),
]
