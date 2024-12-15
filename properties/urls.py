from django.urls import path
from .views import (
    PropertyListCreateView, PropertyDetailView,
    BookingListCreateView, BookingDetailView,
    ImageListCreateView, ImageDetailView,
    ReviewListCreateView, ReviewDetailView, get_all_properties
)

urlpatterns = [
    path('', PropertyListCreateView.as_view(), name='property-list-create'),
    path('all', get_all_properties, name='property-list'),
    path('<int:pk>/', PropertyDetailView.as_view(), name='property-detail'),

    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),

    path('images/', ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
