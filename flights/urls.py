from django.urls import path
from .views import AirportListCreateView, AirportDetailView, FlightDetailView, FlightListCreateView

urlpatterns = [
    path("airport/", AirportListCreateView.as_view(), name="airport-list-create"),
    path("airport/<int:pk>/", AirportDetailView.as_view(), name="airport-detail"),
    path('', FlightListCreateView.as_view(), name='flight-list-create'),
    path('<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
]
