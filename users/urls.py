from django.urls import path
from .views import UserListCreateView, UserDetailView, UserCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
]
