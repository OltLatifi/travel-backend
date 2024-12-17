from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),

    path("api/users/", include("users.urls")),
    path("api/flights/", include("flights.urls")),
    path("api/properties/", include("properties.urls")),
    path("api/vehicles/", include("vehicles.urls")),
    path("api/payments/", include("payments.urls")),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
