from django.urls import path
from .views import (
    BookingListCreateView, BookingDetailView,
    PropertyView,
    ReviewListCreateView, ReviewDetailView, get_all_properties, update_property_availability
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PropertyView, basename='property')

urlpatterns = [
    path('all', get_all_properties, name='property-list'),

    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('<int:property_id>/update-availability/', update_property_availability, name='update-property-availability'),
]

urlpatterns += router.urls