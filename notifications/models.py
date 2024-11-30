# notifications/models.py
from django.db import models
from users.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    content = models.TextField()
    read_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
