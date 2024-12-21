from django.urls import path
from .views import get_notifications, mark_notification_as_read

urlpatterns = [
    path('', get_notifications, name='get-notifications'),
    path('<int:notification_id>/mark-as-read/', mark_notification_as_read, name='mark-notification-as-read'),
]